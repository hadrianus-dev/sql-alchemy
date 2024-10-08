# pylint: disable=C0301
# pylint: disable=E0239
# pylint: disable=C0412

from typing import List
from sqlalchemy.orm import Mapped, registry, mapped_column, relationship
from sqlalchemy import Table
from sqlalchemy import Column, ForeignKey, String

mapper_registry = registry()

filmes_genres_association = Table(
    "films_genres",
    mapper_registry.metadata,
    Column("film_id", ForeignKey("films.id")),
    Column("right_id", ForeignKey("genres.id")),
)

@mapper_registry.mapped
class Genres:
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))

    films: Mapped[List["Film"]] = relationship("Film", secondary=filmes_genres_association, back_populates="genres")  # noqa: F821

    def __repr__(self):
        return f"Genre: [id={self.id}, title={self.title}, description={self.description}]"
