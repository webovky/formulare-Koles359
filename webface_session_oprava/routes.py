from . import app
from flask import render_template, request, Flask, session, redirect, url_for
from datetime import timedelta
from pony.orm import db_session
from .models import Zkracovac
from random import choice
import functools

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if "user" in session:
           return func(*args, **kwargs)
        else: 
            return redirect(url_for("login"))

    return wrapper

@app.route("/login/", methods=["POST", "GET"])
def login():
    title = "Login"
    if request.method == "POST":
        session.permanent = True
        user  =request.form["nm"]
        session["user"] = user
        return redirect(url_for("index"))
    else:
        if "user" in session:
            return redirect(url_for("index"))
        return render_template("login_user.html.j2", title=title)

@app.route("/user/")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout/")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
     
@app.route("/")
@login_required
def index():
    title = "Index"
    return render_template("base.html.j2", title=title)


@app.route("/trojuhelnik/")
@login_required
def trojuhelnik():
    title = "Trojúhelník"
    a = request.args.get("a")
    b = request.args.get("b")
    c = request.args.get("c")
    try:
        o = int(a) + int(b) + int(c)
    except (TypeError, ValueError):
        o = ""
    return render_template("trojuhelnik.html.j2", title=title, o=o)

@app.route("/ctverec/")
@login_required
def ctverec():
    title = "Čtverec"
    a = request.args.get("a")
    try:
        o = 4*int(a)
        s = int(a)*int(a)
    except (TypeError, ValueError):
        o = ""
        s = ""
    return render_template("ctverec.html.j2", title=title, o=o, s=s)

@app.route("/obdelnik/")
@login_required
def obdelnik():
    title = "Obdélník"
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        o = 2*(int(a)+int(b))
        s = int(a)*int(b)
    except (TypeError, ValueError):
        o = ""
        s = ""
    return render_template("obdelnik.html.j2", title=title, o=o, s=s)


@app.route('/zkracovac', methods=["GET", "POST"])
@login_required
@db_session
def zkracovac():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            existing = Zkracovac.get(url = url)
            if existing:
                zkratka = existing.zkratka
            else:
                pismena = "qwertzuiopasdfghjklyxcvbnm"
                zkratka = "" 
                for i in range(7):
                    i = choice(pismena)
                    zkratka += i
                Zkracovac(url = url, zkratka = zkratka)
            return render_template("zkracovac.html.j2", zprava = f"{request.url}/{zkratka}")
        else:
            return render_template("zkracovac.html.j2")

    else:
        return render_template("zkracovac.html.j2")


@app.route('/zkracovac/<string:zkratka>')
@db_session
def zkracovac_redirect(zkratka):
    url = Zkracovac.get(zkratka=zkratka).url
    return redirect(url)