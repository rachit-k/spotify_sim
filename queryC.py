from codeval import code2val, pcode2val, lcode2val, tcode2val

def queryCreatorHelper(form, where_head):
    song = form.get("song")
    if(not ( song is None or  not song)):
        where_head = where_head + " and song_name='"+song+"' "
    attributeList = [ "Danceability", "Acousticness", "Energy", "Instrumentalness", "Liveness", "Speechiness"]
    attributeList2 = ["Loudness", "Tempo"]
    for attr in attributeList:
        attval = form.get(attr)
        if(not ( attval is None or  not attval)):
            where_head = where_head + " and " + attr + ">=" +str(code2val(attval)[0])+ " and " +attr + "<" +str(code2val(attval)[1])
    p = "song_pop"
    attval = form.get("Popularity")
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
    head = 'select song_name, song_link from song'
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
