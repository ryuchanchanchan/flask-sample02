import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/omikuji")
def mikuji():
    result = random.choice(["大吉", "吉", "凶"])
    return render_template("omikuji.html", result=result)


@app.route("/members")
def members():
    members = ["Bob", "Tom", "Ken"]
    return render_template("members.html", members=members)
if __name__ == "__main__":
    app.run(debug=True)
