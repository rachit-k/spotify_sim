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

def queryCreator(form):
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

def DelQueryCreatorName(form):
    song = form.get("Song")
    return "delete from song where song_name = "+song

def DelQueryCreatorLink(form):
    song = form.get("Link")
    return "delete from song where link = "+song

def valueCreator(attrlist):
    ret = ""
    ret = ret + str(attrlist)[1:-1] +");"
    return ret
def InsQueryCreatorLink(form):
    link = form.get("Link")
    id = link.split("/")[-1]
    song_db, song_art_db, alb_art_db, album_db, artist_db, genre_db = getAttributes(id)
    print(song_db)
    #song insert
    song_query = "Insert into song values (" + valueCreator(song_db)
    #artist insert
    artist_query = ""
    for a in artist_db:
        artist_query =  artist_query + "Insert into artist values ("+valueCreator(a) +"\n"
    #album insert
    album_query = "Insert into album values ("+valueCreator(album_db)
    #song_artist insert
    song_art_query = ""
    for atlist in song_art_db:
        song_art_query = song_art_query + "Insert into artist_song values (" + valueCreator(atlist)+"\n"
    #album_artist insert
    album_art_query = ""
    for atlist in alb_art_db:
        album_art_query = album_art_query + "Insert into album_artist values (" + valueCreator(atlist)+"\n"
    #genre_db insert
    art_genre_query = ""
    for atlist in genre_db:
        art_genre_query = art_genre_query + "Insert into artist_genre values (" + valueCreator(atlist)+"\n"
    return "BEGIN;" + "\n" + artist_query + album_query+ "\n" + song_query + "\n" + song_art_query + album_art_query + art_genre_query +"COMMIT;"

    