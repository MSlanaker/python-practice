# Practice with sessions and cookies

from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")


@app.route("/user")
def user():
    return f"<h1><h1>"


if __name__ == "__main__":
    app.run(debug=True)
