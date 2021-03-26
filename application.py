from flask import Flask, render_template, request
import psycopg2 
import sys

app = Flask(__name__)

app.config['dbname'] = "sample" #sys.argv[1]
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
def code2val(code):
    if(code=="0"):
        return [0,0.2]
    if(code=="1"):
        return [0.2,0.4]
    if(code=="2"):
        return [0.4, 0.6]
    if(code=="3"):
        return [0.6, 0.8]
    if(code=="4"):
        return [0.8,1.1]

def pcode2val(code):
    if(code=="0"):
        return [0,20]
    if(code=="1"):
        return [20,40]
    if(code=="2"):
        return [40, 60]
    if(code=="3"):
        return [60, 80]
    if(code=="4"):
        return [80,101]

def lcode2val(code):
    if(code=="0"):
        return [4,-5]
    if(code=="1"):
        return [-5,-17]
    if(code=="2"):
        return [-17, -29]
    if(code=="3"):
        return [-29, -42]
    if(code=="4"):
        return [-42,-55]

def tcode2val(code):
    if(code=="0"):
        return [0,30]
    if(code=="1"):
        return [30,60]
    if(code=="2"):
        return [60, 90]
    if(code=="3"):
        return [90, 150]
    if(code=="4"):
        return [150,240]
def queryCreator(form):
    head = 'select song_name from song'
    where_head = " where true"
    attributeList = [ "Danceability", "Acousticness", "Energy", "Instrumentalness", "Liveness", "Speechiness"]
    attributeList2 = ["Loudness", "Tempo"]
    for attr in attributeList:
        attval = form.get(attr)
        if(not ( attval is None or  not attval)):
            where_head = where_head + " and " + attr + ">=" +str(code2val(attval)[0])+ " and " +attr + "<" +str(code2val(attval)[1])
    p = "Popularity"
    attval = form.get(p)
    if(not ( attval is None or  not attval)):
        where_head = where_head + " and " + p + ">=" +str(pcode2val(attval)[0])+ " and " +p + "<" +str(pcode2val(attval)[1])
    l = "Loudness"
    attval = form.get(l)
    if(not ( attval is None or  not attval)):
        where_head = where_head + " and " + l + "<=" +str(lcode2val(attval)[0])+ " and " +l + ">" +str(lcode2val(attval)[1])
    t = "Tempo"
    attval = form.get(t)
    if(not ( attval is None or  not attval)):
        where_head = where_head + " and " + t + ">=" +str(tcode2val(attval)[0])+ " and " +t + "<" +str(tcode2val(attval)[1])
    return head+where_head + " limit 10"


@app.route("/", methods=["GET"])
def welcome():
    return render_template("welcome.html")

@app.route("/input", methods=["GET"])
def input():
    return render_template("inpage.html")

@app.route("/output", methods=["POST"])
def output():
    # command = request.form.get("name")
    # print(command)
    command = queryCreator(request.form)
    print(command)
    cur.execute(command)
    records = cur.fetchall()
    return render_template("outpage.html", name=str(records))