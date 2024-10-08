# pylint: disable=C0301

from typing import List
from sqlalchemy.orm import Mapped, registry, mapped_column, relationship
from sqlalchemy import Integer, String
from sqlalchemy import Table
from sqlalchemy import Column, ForeignKey

#from src.infra.entities.genres import Genres
#from src.infra.entities import Genre

mapper_registry = registry()

""" filmes_genres_association = Table(
    "films_genres",
    mapper_registry.metadata,
    Column("film_id", ForeignKey("films.id")),
    Column("right_id", ForeignKey("genres.id")),
) """

@mapper_registry.mapped
class Films:
    __tablename__ = "films"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))
    year: Mapped[int] = mapped_column(Integer)
    #genres: Mapped[List["Genre"]] = relationship("Genre", secondary=filmes_genres_association, back_populates="films")

    def __repr__(self):
        return f"Film: [id={self.id}, title={self.title}, description={self.description}, year={self.year}]"
