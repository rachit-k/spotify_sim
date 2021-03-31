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

create materialized view my_genre_view as
select a.artist_id, artist_name, link as artist_link, image_link, popularity, artist_type, followers, array_agg(genre) as genres
from artist as a, artist_genre as g
where a.artist_id = g.artist_id group by a.artist_id;

create view simple_genre_view as
select artist_id, artist_name, artist_link, image_link, popularity, artist_type, followers, unnest(genres) as genre
from my_genre_view;


create materialized view song_year as
select song_id, song_name, date_part('year', release_date) as year, song.popularity, song.link as song_link
from song, album
where song.album_id=album.album_id;

create materialized view pop_year_song as
select song_id, song_name, song_link, popularity, year, row_number() over (partition by year order by popularity desc, song_name, song_id) as rank from song_year order by year;

create materialized view pop_year_album as
select album_id, album_name, link as album_link, popularity, date_part('year', release_date) as year, row_number() over (partition by date_part('year', release_date) order by popularity desc, album_name, album_id) as rank from album order by year;