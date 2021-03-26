from flask import Flask, render_template, request
import psycopg2 
import sys

app = Flask(__name__)

app.config['dbname'] = "db" #sys.argv[1]
app.config['user'] = "postgres" #sys.argv[2]
dbname = app.config.get('dbname')
user = app.config.get('user')
# app.config['password'] = "147895362" #sys.argv[3]
# password = app.config.get('password')
# connect = ("dbname="+dbname+ " user="+user+ " password="+password)
connect = ("dbname="+dbname+ " user="+user)
print(connect)
conn = psycopg2.connect(connect)
cur = conn.cursor()
print("We are here")
app.run()

# @app.route("/", methods=["GET", "POST"])
# def inpage():
#     if request.method == "POST":
#         command = request.form.get("name")
#         print(command)
#         cur.execute(command)
#         records = cur.fetchall()
#         return render_template("outpage.html", name=str(records))
#     return render_template("inpage.html")

# if __name__ == '__main__':


@app.route("/", methods=["GET"])
def input():
    return render_template("inpage.html")

@app.route("/output", methods=["POST"])
def output():
    command = request.form.get("name")
    print(command)
    cur.execute(command)
    records = cur.fetchall()
    return render_template("outpage.html", name=str(records))