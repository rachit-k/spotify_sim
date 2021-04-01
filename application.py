from flask import Flask, render_template, request
from queryC import queryCreatorSong, InsQueryCreatorLink, DelQueryCreator, getGenresTrends, getYearSongTrends, getYearAlbumTrends
import psycopg2 
import sys

app = Flask(__name__)

app.config['dbname'] = "db" #sys.argv[1]
app.config['user'] = "postgres" #sys.argv[2]
dbname = app.config.get('dbname')
user = app.config.get('user')
app.config['password'] = "qmwnebrv1234" #sys.argv[3]
password = app.config.get('password')
# connect = ("dbname="+dbname+ " user="+user+ " password="+password)
connect = ("dbname="+dbname+ " user="+user)
print(connect)
conn = psycopg2.connect(connect)
cur = conn.cursor()
@app.route("/", methods=["GET"])
def welcome():
    return render_template("welcome.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("inpage.html")

@app.route("/delete", methods=["GET"])
def delete():
    return render_template("delete.html")

@app.route("/addsong", methods=["GET"])
def addsong():
    return render_template("addsong.html")

@app.route("/addartist", methods=["GET"])
def addartist():
    return render_template("addartist.html")

@app.route("/addalbum", methods=["GET"])
def addalbum():
    return render_template("addalbum.html")

@app.route("/addusinglink", methods=["GET"])
def addusinglink():
    return render_template("addusinglink.html")

@app.route("/trendgenre", methods=["GET"])
def trendgenre():
    return render_template("trendgenre.html")

@app.route("/trendsong", methods=["GET"])
def trendartist():
    return render_template("trendsong.html")

@app.route("/trendalbum", methods=["GET"])
def trendalbum():
    return render_template("trendalbum.html")

@app.route("/addsuccess", methods=["POST"])
def addsuccess():
    print("Here we are")
    command = InsQueryCreatorLink(request.form)
    print(command)
    cur.execute(command)
    return render_template("addsuccess.html")

@app.route("/addfailure", methods=["POST"])
def addfailure():
    return render_template("addfailure.html")

@app.route("/deletesuccess", methods=["POST"])
def deletesuccess():
    command = DelQueryCreator(request.form)
    print(command)
    cur.execute(command)
    return render_template("deletesuccess.html")

@app.route("/deletefailure", methods=["POST"])
def deletefailure():
    return render_template("deletefailure.html")

@app.route("/output", methods=["POST"])
def output():
    command = queryCreatorSong(request.form)
    print(command)
    cur.execute(command)
    records = cur.fetchall()
    return render_template("outpage.html", name=(records))

@app.route("/outputtrgenres", methods=["POST"])
def outputGenres():
    command = getGenresTrends(request.form)
    print(command)
    cur.execute(command)
    records = cur.fetchall()
    return render_template("outputtrgenres.html", name=(records))

@app.route("/outputtrsong", methods=["POST"])
def outputSong():
    command = getYearSongTrends(request.form)
    print(command)
    cur.execute(command)
    records = cur.fetchall()
    return render_template("outputtrsong.html", name=(records))

@app.route("/outputtralbum", methods=["POST"])
def outputAlbum():
    command = getYearAlbumTrends(request.form)
    print(command)
    cur.execute(command)
    records = cur.fetchall()
    return render_template("outputtralbum.html", name=(records))