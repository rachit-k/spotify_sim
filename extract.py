import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_id = '6b12024ce0504135b6d831be01039fb3'
client_secret = '58fb545eb53140bc9c76e0cf64a68654'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=20)
def getAttributes(id):
    meta = sp.track(id)
    myartists = {""}
    features = sp.audio_features(id)
    # meta
    name = meta['name']
    #link = 
    album_id = meta['album']['id']
    artists = meta['artists']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    link = meta['external_urls']['spotify']
    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    track = [id, name, album_id, link, length, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    song_artists = artists
    
    song_artdb = []
    alb_artdb = []
    for a in song_artists:
        song_artdb.append([id, a['id']])
        myartists.add(a['id'])
    
    album = sp.album(album_id)
    albumfeature = [album['id'],album['type'],album['name'],album['external_urls']['spotify'], album['popularity'], album['release_date'], album['release_date_precision'], album['label'], album['total_tracks']]
    alb_artists = album['artists']
    artist_db = []
    genre_db = []
    for a in alb_artists:
        alb_artdb.append ([ album_id, a['id']])
        myartists.add(a['id'])
    myartists.remove("")
    for art in myartists:
        myart = sp.artist(art)
        img = ''
        if(len(myart['images'])>0):
            img = myart['images'][0]['url']
        artist_db.append([myart['id'], myart['name'], myart['external_urls']['spotify'], img, myart['popularity'], myart['type'], myart['followers']['total']])
        for g in myart['genres']:
            genre_db.append([myart['id'], g])
    return track, song_artdb, alb_artdb, albumfeature, artist_db, genre_db