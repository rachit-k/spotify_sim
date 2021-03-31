from codeval import code2val, pcode2val, lcode2val, tcode2val
from extract import getAttributes
def queryCreatorHelper(form, where_head):
    song = form.get("Song")
    if(not ( song is None or  not song)):
        where_head = where_head + " and song_name='"+song+"' "
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
    return where_head

def queryCreatorEmpty(form):
    head = 'select song_name, link from song'
    where_head = " where true"
    return head+ queryCreatorHelper(form, where_head) + " limit 10"

def queryCreatorAlbum(form, album):
    head = 'select song_name, song_link from songalbum'
    where_head = " where album_name = '"+album+"'"
    return head+ queryCreatorHelper(form, where_head) + " limit 10"

def queryCreatorArtist(form, artist):
    head = 'select song_name, song_link from songart'
    where_head = " where artist_name = '"+artist+"'"
    return head+ queryCreatorHelper(form, where_head) + " limit 10"

def queryCreatorArtistAlbum(form, artist, album):
    head = 'select song_name, song_link from songart, songalbum'
    where_head = "where songart.song_id=songalbum.song_id "
    where_head = where_head + " and artist_name = '"+artist+"'"
    where_head = where_head + " and album_name = '"+album+"'"
    return head+ queryCreatorHelper(form, where_head) + " limit 10"

def queryCreatorSong(form):
    artist = form.get("Artist")
    album = form.get("Album")
    if((artist is None or not artist) and (album is None or not album)):
        return queryCreatorEmpty(form)
    elif (artist is None or not artist):
        return queryCreatorAlbum(form, album)
    elif (album is None or not album):
        return queryCreatorArtist(form, artist)
    else:
        return queryCreatorArtistAlbum(form, artist, album)

def DelQueryCreatorName(song):
    return "delete from song where song_name = '"+song +"';"

def DelQueryCreatorLink(link):
    return "delete from song where link = '"+link +"';"

def DelQueryCreator(form):
    link = form.get("Song Link")
    song = form.get("Name")
    if(link is None or not link):
        return DelQueryCreatorName(song)
    return DelQueryCreatorLink(link)
def valueCreator(attrlist):
    ret = ""
    ret = ret + str(attrlist)[1:-1] +")"
    return ret
def InsQueryCreatorLink(form):
    link = form.get("Song Link")
    id = link.split("/")[-1]
    addendum = ' ON CONFLICT DO NOTHING;'
    song_db, song_art_db, alb_art_db, album_db, artist_db, genre_db = getAttributes(id)
    print(song_db)
    #song insert
    song_query = "Insert into song values (" + valueCreator(song_db) + addendum
    #artist insert
    artist_query = ""

    for a in artist_db:
        artist_query =  artist_query + "Insert into artist values ("+valueCreator(a) + addendum +"\n"
    #album insert
    album_query = "Insert into album values ("+valueCreator(album_db) +addendum
    #song_artist insert
    song_art_query = ""
    for atlist in song_art_db:
        song_art_query = song_art_query + "Insert into artist_song values (" + valueCreator(atlist)+addendum+"\n"
    #album_artist insert
    album_art_query = ""
    for atlist in alb_art_db:
        album_art_query = album_art_query + "Insert into album_artist values (" + valueCreator(atlist)+addendum+"\n"
    #genre_db insert
    art_genre_query = ""
    for atlist in genre_db:
        art_genre_query = art_genre_query + "Insert into artist_genre values (" + valueCreator(atlist)+addendum+"\n"
    return "BEGIN;" + "\n" + artist_query + album_query+ "\n" + song_query + "\n" + song_art_query + album_art_query + art_genre_query +"COMMIT;"

def getGenresQueryCreator(minfol, maxfol, pop):
    head = "select genre, count(genre) from simple_genre_view"
    where_head = "where true"
    if(minfol is not None and minfol):
        where_head = where_head + "and followers >="+str(minfol)
    if(maxfol is not None and maxfol):
        where_head = where_head + "and followers >="+str(maxfol)
    p = "Popularity"
    attval = pop
    if(not ( attval is None or  not attval)):
        where_head = where_head + " and " + p + ">=" +str(pcode2val(attval)[0])+ " and " +p + "<" +str(pcode2val(attval)[1])
    return head+where_head +"order by count desc limit 10;"

def getYearSongTrends(form):
    start = form.get('From')
    end = form.get('To')
    num = form.get('Num')
    if(num is None or not num):
        num = 3
    else:
        num = int(num)
    query = 'select song_id, song_name, song_link from pop_year_song'
    where_head = "where rank<="+str(num)
    where_head = where_head + " and year <="+str(end) + " and year>="+str(start)
    return query+where_head

def getYearAlbumTrends(form):
    start = form.get('From')
    end = form.get('To')
    num = form.get('Num')
    if(num is None or not num):
        num = 3
    else:
        num = int(num)
    query = 'select album_id, album_name, album_link from pop_year_album'
    where_head = "where rank<="+str(num)
    where_head = where_head + " and year <="+str(end) + " and year>="+str(start)
    return query+where_head
