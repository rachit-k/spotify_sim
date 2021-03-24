# Greets user via a form using POST, a layout, and a single route

from flask import Flask, render_template, request
import psycopg2 
import sys
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def inpage():
    if request.method == "POST":
        command = request.form.get("name")
        print(command)
        cur.execute(command)
        records = cur.fetchall()
        return render_template("outpage.html", name=str(records)) #form=post
    return render_template("inpage.html")
if __name__ == '__main__':
    app.config['dbname'] = sys.argv[1]
    app.config['user'] = sys.argv[2]
    app.config['password'] = sys.argv[3]
    dbname = app.config.get('dbname')
    user = app.config.get('user')
    password = app.config.get('password')
    connect = ("dbname="+dbname+ " user="+user+ " password="+password)
    print(connect)
    conn = psycopg2.connect(connect)
    cur = conn.cursor()
    print("We are here")
    app.run()
# @app.route("/", methods=["GET"])
# def input():
#     return render_template("inpage.html")

# @app.route("/page2", methods=["POST"])
# def output():
#     return render_template("outpage.html", name=request.form.get("name")) 