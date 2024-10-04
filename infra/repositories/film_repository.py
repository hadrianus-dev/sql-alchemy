# pylint: disable=E0239
from infra.config.connection import DBConnectionHandler
from infra.entities.films import Film

class FilmRepository:

    def select(self):
        with DBConnectionHandler() as db:
            result = db.session.query(Film).all()
            return result

    def insert(self, title: str, description: str, genre: str, year: int):
        with DBConnectionHandler() as db:
            film = Film(title=title, description=description, genre=genre, year=year)
            db.session.add(film)
            db.session.commit()

    def update(self, id: int, title: str, description: str, genre: str, year: int):
        with DBConnectionHandler() as db:
            db.session.query(Film).filter(Film.id == id).update({Film.title: title, Film.description: description, Film.genre: genre, Film.year: year})
            db.session.commit()

    def delete(self, id: int):
        with DBConnectionHandler() as db:
            db.session.query(Film).filter(Film.id == id).delete()
            db.session.commit()
