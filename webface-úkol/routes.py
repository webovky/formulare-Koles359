from . import app
from flask import render_template
from flask import request





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


@app.route("/text/")
def text():
    return """

<h1>Text</h1>

<p>toto je text</p>

"""
