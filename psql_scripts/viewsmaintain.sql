Create Materialized View songalbum as
Select song_id, song_name, song.album_id, song.link as song_link, length, song.popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, type_album, album_name, album.link as album_link, album.popularity as al_pop, release_date, label
from song, album
where song.album_id = album.album_id;

Create index song_name_index 
On songalbum(song_name);

Create index song_id_index 
On songalbum using hash (song_id);

Create index album_id_index
On songalbum using hash (album_id);

Create index album_name_index
On songalbum(album_name);

Create index release_date_index
On songalbum(release_date);

Create index label_index
On songalbum using hash (label);

Create index type_album_index 
On songalbum using hash (type_album);

--to be only used for searching based on song--
Create Materialized View songart as
Select song.song_id, song_name, song.album_id, song.link as song_link, length, song.popularity , danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, artist.artist_id, artist_name, artist.link as artist_link, image_link, artist.popularity as art_pop, artist_type, followers
From song, artist, artist_song
Where song.song_id=artist_song.song_id and artist.artist_id=artist_song.artist_id;

Create index song_name_index2 
On songart(song_name);

Create index song_id_index2
On songart(song_id);

Create index artist_type_index 
On songart using hash (artist_type);

Create index artist_id_index
On songart using hash(artist_id);

Create index artist_name_index
On song(artist_name);

--choice to have this
Select song.song_id, song_name, song.album_id, song.link as song_link, length, song.popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, artist.artist_id, artist_name, artist.link as artist_link, image_link, artist.popularity as art_pop, artist_type, followers, type_album, album_name, album.link as album_link, album.popularity as al_pop, release_date, label
From song, artist, album, artist_song
Where song.song_id=artist_song.song_id and artist.artist_id=artist_song.artist_id and song.album_id=album.album_id;
