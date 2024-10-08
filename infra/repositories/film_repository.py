# pylint: disable=E0239
# pylint: disable=C0301
from infra.config.connection import DBConnectionHandler
from infra.entities.films import Films as Film

class FilmRepository:

    def select(self):
        with DBConnectionHandler() as db:
            try:
                result = db.session.query(Film).all()
                return result
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, title: str, description: str,year: int):
        with DBConnectionHandler() as db:
            try:
                film = Film(title=title, description=description, year=year)
                db.session.add(film)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, id: int, title: str, description: str, year: int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Film).filter(Film.id == id).update({Film.title: title, Film.description: description, Film.year: year})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id: int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Film).filter(Film.id == id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
