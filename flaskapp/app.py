from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/confirm")
def confirm():
    return render_template("confirm.html", name=request.args.get("bitcoin address"))
