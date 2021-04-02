SET datestyle = dmy;
create table albumtemp (
    album_id text,
    type_album text,
    album_name text,
    link text,
    popularity bigint,
    release_date date,
    precision_date text,
    label text,
    num_tracks bigint
);
create table album (
    album_id text,
    type_album text,
    album_name text,
    link text,
    popularity bigint,
    release_date date,
    precision_date text,
    label text,
    num_tracks bigint,
    constraint album_key primary key(album_id)
);
create table artiststemp (
    artist_id text,
    artist_name text,
    link text,
    image_link text,
    popularity bigint,
    artist_type text,
    followers bigint
);
create table artist (
    artist_id text,
    artist_name text,
    link text,
    image_link text,
    popularity bigint,
    artist_type text,
    followers bigint,
    constraint artist_key primary key(artist_id)
);
create table song(
    song_id text,
    song_name text,
    album_id text,
    link text,
    length bigint,
    Popularity bigint,
    Danceability double precision,
    Acousticness double precision,
    Energy double precision,
    Instrumentalness double precision,
    Liveness double precision,
    Loudness double precision,
    Speechiness double precision,
    Tempo double precision,
    Time_signature bigint,
    constraint song_key primary key(song_id),
    constraint album_ref foreign key(album_id) references album(album_id)
);
create table songstemp(
    song_id text,
    song_name text,
    album_id text,
    link text,
    length bigint,
    Popularity bigint,
    Danceability double precision,
    Acousticness double precision,
    Energy double precision,
    Instrumentalness double precision,
    Liveness double precision,
    Loudness double precision,
    Speechiness double precision,
    Tempo double precision,
    Time_signature bigint,
    constraint album_ref foreign key(album_id) references album(album_id)
);
create table album_artisttemp(
    album_id text,
    artist_id text,
    constraint album_ref foreign key(album_id) references album(album_id),
    constraint artist_ref foreign key(artist_id) references artist(artist_id)
);
create table album_artist(
    album_id text,
    artist_id text,
    constraint album_artist_key primary key(album_id, artist_id),
    constraint album_ref foreign key(album_id) references album(album_id),
    constraint artist_ref foreign key(artist_id) references artist(artist_id)
);
create table artist_songtemp(
    song_id text,
    artist_id text,
    constraint song_ref foreign key(song_id) references song(song_id),
    constraint artist_ref foreign key(artist_id) references artist(artist_id)
);
create table artist_song(
    song_id text,
    artist_id text,
    constraint artist_song_key primary key(song_id, artist_id),
    constraint song_ref foreign key(song_id) references song(song_id),
    constraint artist_ref foreign key(artist_id) references artist(artist_id)
);
create table artist_genretemp(
    artist_id text,
    genre text,
    constraint artist_ref foreign key(artist_id) references artist(artist_id)
);
create table artist_genre(
    artist_id text,
    genre text,
    constraint artist_genre_key primary key(artist_id, genre),
    constraint artist_ref foreign key(artist_id) references artist(artist_id)
);

\copy albumtemp from '../../MyData/album_dbc.csv' delimiter ',' csv header;
insert into album select distinct on (album_id)  * from albumtemp;
drop table albumtemp;


\copy artiststemp from '../../MyData/artist_db.csv' delimiter ',' csv header;
insert into artist select distinct on (artist_id)  * from artiststemp;
drop table artiststemp;


\copy songstemp from '../../MyData/song_db.csv' delimiter ',' csv header;
insert into song select distinct on (song_id)  * from songstemp;
drop table songstemp;

\copy album_artisttemp from '../../MyData/album_artist.csv' delimiter ',' csv header;
insert into album_artist select distinct on (album_id,artist_id)  * from album_artisttemp;
drop table album_artisttemp;


\copy artist_songtemp from '../../MyData/artist_song.csv' delimiter ',' csv header;
insert into artist_song select distinct on (song_id,artist_id)  * from artist_songtemp;
drop table artist_songtemp;


\copy artist_genretemp from '../../MyData/genre_artist.csv' delimiter ',' csv header;
insert into artist_genre select distinct on (artist_id, genre)  * from artist_genretemp;
drop table artist_genretemp;

---alterations--
alter table artist_song
drop constraint song_ref,
add constraint song_ref foreign key(song_id) references song(song_id)  on delete cascade DEFERRABLE;

alter table artist_song
drop constraint artist_ref,
add constraint artist_ref foreign key(artist_id) references artist(artist_id)  on delete cascade DEFERRABLE;

alter table song
drop constraint album_ref,
add constraint album_ref foreign key(album_id) references album(album_id) on delete set NULL DEFERRABLE;

alter table album_artist
drop constraint song_ref,
add constraint song_ref foreign key(song_id) references song(song_id)  on delete cascade DEFERRABLE;

alter table album_artist
drop constraint artist_ref,
add constraint artist_ref foreign key(artist_id) references artist(artist_id)  on delete cascade DEFERRABLE;

alter table artist_genre
drop constraint artist_ref,
add constraint artist_ref foreign key(artist_id) references artist(artist_id)  on delete cascade  on update set null DEFERRABLE;