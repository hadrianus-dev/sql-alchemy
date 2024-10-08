# pylint: disable=C0301
from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# setting up connection
engine = create_engine("mysql+pymysql://root@localhost:3306/cinema", echo=True)
session = Session(engine)

class Base(DeclarativeBase):
    pass

# Film model
class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(255))
    genre = Column(String(255))
    year = Column(Integer)

    def __repr__(self):
        return f"Film (id={self.id}, title={self.title}, description={self.description}, genre={self.genre}, year={self.year})"

# INSERT
""" new_film = Film(title="The Matrix", description="Um filme de ação", genre="Ação", year=1999)
session.add(new_film)
session.commit()
print({'INSERT': new_film})
print() """

# INSERT MANY
""" films = [
    Film(title="The Chain", description="Um filme de ação", genre="Ação", year=1999),
    Film(title="The Master", description="Um filme de ação", genre="Ação", year=2001),
    Film(title="Deadpool 2", description="Um filme de ação", genre="Ação", year=2018),
    Film(title="The One", description="Um filme de ação", genre="Ação", year=2000),
    Film(title="Dane The Dog", description="Um filme de ação", genre="Ação", year=2006),
]
session.add_all(films)
session.commit()
print() """


# UPDATE
# stmt = select(Film).where(Film.title == "The Matrix")
# result = session.scalars(stmt).one()
result = session.get(Film, 3)
result.title = "The Matrix Resurrections"
session.commit()
print({'UPDATE': result})
print()
# OR
# session.query(Film).filter(Film.title == "The Matrix").update({"title": "The Matrix Resurrections"})
# session.commit()

# DELETE
stmt = select(Film).where(Film.title == "The Matrix Resurrections")
result = session.scalars(stmt).one()
session.delete(result)
session.commit()
print({'DELETE': result})
print()
# OR
# session.query(Film).filter(Film.title == "The Matrix Resurrections").delete()
# session.commit()

""" all_data = session.query(Film).all()
print({'GET ALL': all_data})
print() """

# SELECT
""" stmt = select(Film).where(Film.title == "Vandame Cabeludo")
result = session.scalars(stmt).all()
print({'SELECTD RESULT': result})
print() """
