# pylint: disable=C0301
from sqlalchemy import create_engine, select, text
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# setting up connection
engine = create_engine("mysql+pymysql://root@localhost:3306/cinema", echo=True)
session = Session(engine)

""" 

CREATE TABLE IF NOT EXISTS genres (
        id int NOT NULL AUTO_INCREMENT,
        title varchar(100) NOT NULL,
        description varchar(255) NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE IF NOT EXISTS films (
        id int NOT NULL AUTO_INCREMENT,
        title varchar(100) NOT NULL,
        description varchar(255) NULL,
        year int NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE IF NOT EXISTS films_genres (
        id int NOT NULL AUTO_INCREMENT,
        film_id int NOT NULL,
        genre_id int NOT NULL,
        PRIMARY KEY (id)
        FOREIGN KEY (film_id) REFERENCES films(id),
        FOREIGN KEY (genre_id) REFERENCES genres(id)
    );

CREATE TABLE IF NOT EXISTS actors (
        id int NOT NULL AUTO_INCREMENT,
        name varchar(100) NOT NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE IF NOT EXISTS films_actors (
        id int NOT NULL AUTO_INCREMENT,
        film_id int NOT NULL,
        actor_id int NOT NULL,
        PRIMARY KEY (id)
        FOREIGN KEY (film_id) REFERENCES films(id),
        FOREIGN KEY (actor_id) REFERENCES actors(id)
    );

INSERT INTO genres (title, description) VALUES ('Ação', 'Filme de ação');
INSERT INTO genres (title, description) VALUES ('Fantasia', 'Filme de fantasia');
INSERT INTO genres (title, description) VALUES ('Terror', 'Filme de terror');

INSERT INTO films (title, description, year) VALUES ('The Matrix', 'Um filme de ação', 1999);
INSERT INTO films (title, description, year) VALUES ('The Matrix Resurrections', 'Um filme de ação', 2021);
INSERT INTO films (title, description, year) VALUES ('Deadpool 2', 'Um filme de ação', 2018);

INSERT INTO actors (name) VALUES ('Keanu Reeves');
INSERT INTO actors (name) VALUES ('Laurence Fishburne');
INSERT INTO actors (name) VALUES ('Carrie-Anne Moss');

INSERT INTO films_genres (film_id, genre_id) VALUES (1, 1);
INSERT INTO films_genres (film_id, genre_id) VALUES (1, 2);
INSERT INTO films_genres (film_id, genre_id) VALUES (2, 1);
INSERT INTO films_genres (film_id, genre_id) VALUES (2, 2);
INSERT INTO films_genres (film_id, genre_id) VALUES (3, 1);

INSERT INTO films_actors (film_id, actor_id) VALUES (1, 1);
INSERT INTO films_actors (film_id, actor_id) VALUES (1, 2);
INSERT INTO films_actors (film_id, actor_id) VALUES (2, 1);
INSERT INTO films_actors (film_id, actor_id) VALUES (2, 2);
INSERT INTO films_actors (film_id, actor_id) VALUES (3, 3);

"""
