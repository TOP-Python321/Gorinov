drop database if exists mus_library;

create database mus_library;

use mus_library;

create table singers (
    id mediumint unsigned primary key auto_increment,
    singer varchar(100) not null unique
);

create table styles (
    id mediumint unsigned primary key auto_increment,
    style varchar(50) not null 
);

create table publishers (
    id mediumint unsigned primary key auto_increment,
    publisher varchar(100) not null unique,
    country varchar(100) not null
);

create table collections (
    id mediumint unsigned primary key auto_increment,
    name varchar(50) not null unique,
    date date not null,
    styles_id mediumint unsigned not null,
    publishers_id mediumint unsigned not null,
    foreign key (styles_id) references styles (id),
    foreign key (publishers_id) references publishers (id)
);

create table songs (
    id tinyint unsigned primary key auto_increment,
    song varchar(50) not null,   
    styles_id mediumint unsigned not null,
    singers_id mediumint unsigned not null,
    foreign key (styles_id) references styles (id),
    foreign key (singers_id) references singers (id)
);

create table collections_songs (
    collections_id mediumint unsigned not null,
    songs_id tinyint unsigned not null,    
    primary key (collections_id, songs_id),
    foreign key (collections_id) references collections (id),
    foreign key (songs_id) references songs (id)
);    
