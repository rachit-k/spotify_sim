from codeval import code2val, pcode2val, lcode2val, tcode2val
def queryCreator(form):
    head = 'select song_name, link from song'
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

def queryCreatorA(form, album):
    head = 'select song_name, link from songalbum'
    where_head = " where album_name = "+album
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