from flask import Flask, render_template, request
from queryC import queryCreator, queryCreatorA
import psycopg2 
import sys

app = Flask(__name__)

app.config['dbname'] = "sample" #sys.argv[1]
app.config['user'] = "postgres" #sys.argv[2]
dbname = app.config.get('dbname')
user = app.config.get('user')
app.config['password'] = "qmwnebrv1234" #sys.argv[3]
password = app.config.get('password')
connect = ("dbname="+dbname+ " user="+user+ " password="+password)
# connect = ("dbname="+dbname+ " user="+user)
print(connect)
conn = psycopg2.connect(connect)
cur = conn.cursor()
@app.route("/", methods=["GET"])
def welcome():
    return render_template("welcome.html")

@app.route("/input", methods=["GET"])
def input():
    return render_template("inpage.html")

@app.route("/output", methods=["POST"])
def output():
    command = queryCreator(request.form)
    print(command)
    cur.execute(command)
    records = cur.fetchall()
    return render_template("outpage.html", name=str(records))