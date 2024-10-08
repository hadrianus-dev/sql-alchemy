# pylint: disable=C0411
from __future__ import annotations
from sqlalchemy import Table
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import registry

mapper_registry = registry()

filmes_genres_association = Table(
    "films_genres",
    mapper_registry.metadata,
    Column("film_id", ForeignKey("films.id")),
    Column("right_id", ForeignKey("genres.id")),
)
