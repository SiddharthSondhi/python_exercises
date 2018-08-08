from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/page_1")
def page_1():
    return render_template("page_1.html")

@app.route("/")
def index():
    return redirect(url_for("home"))

app.debug = True
app.run(host="0.0.0.0")
n