from flask import Flask, flash, redirect, render_template, request, session


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stay")
def stay():
    return render_template("stay.html")

@app.route("/see")
def see():
    return render_template("see.html")

@app.route("/dine")
def dine():
    return render_template("dine.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")