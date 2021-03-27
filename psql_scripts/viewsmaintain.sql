Create Materialized View songalbum
Select song_id, song_name, song.album_id, song.link as song_link, length, song.popularity as song_pop, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, type_album, album_name, album.link as album_link, album.popularity as al_pop, release_date, label
from song, album
where song.album_id = album.album_id;

Create index song_name_index 
On songalbum(song_name);

Create index song_id_index 
On songalbum(song_id);

Create index album_id_index
On songalbum(album_id);

Create index album_name_index
On songalbum(album_name);

Create index release_date_index
On songalbum(release_date);

Create index label_index
On songalbum using hash (label);

Create index type_album_index 
On songalbum using hash (type_album)