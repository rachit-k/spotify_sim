# Greets user via a form using POST, a layout, and a single route

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inpage():
    if request.method == "POST":
        return render_template("outpage.html", name=request.form.get("name")) #form=post
    return render_template("inpage.html")

# @app.route("/", methods=["GET"])
# def input():
#     return render_template("inpage.html")

# @app.route("/page2", methods=["POST"])
# def output():
#     return render_template("outpage.html", name=request.form.get("name")) 