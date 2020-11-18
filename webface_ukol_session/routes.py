from . import app
from flask import render_template, request, Flask, session, redirect, url_for
from datetime import timedelta

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/login/", methods=["POST", "GET"])
def login():
    title = "Login"
    if request.method == "POST":
        session.permanent = True
        user  =request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
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
def index():
    title = "Index"
    return render_template("base.html.j2", title=title)


@app.route("/trojuhelnik/")
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




