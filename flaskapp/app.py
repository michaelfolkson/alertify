from flask import Flask, render_template, request

app = Flask(__name__)

ADDRESSES = []
# Should really be a dictionary with username and Bitcoin address

@app.route("/")
def index():
    return render_template("index.html")

# Ensuring form input updates a list/dictionary
# https://youtu.be/oVA0fD13NGI?t=4201

@app.route("/confirm")
def confirm():
    name = request.form.get("name")
    ADDRESSES = name
    return render_template("confirm.html", name=request.args.get("bitcoin address"))

@app.route("/addresses")
def addresses():
    return render_template("addresses.html", addresses=ADDRESSES)
