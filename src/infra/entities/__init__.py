from sqlalchemy.orm import registry
#from .actor import Actor
from .films import Films as Film
from .genres import Genres as Genre
from .associations import filmes_genres_association

mapper_registry = registry()

__all__ = ["Film", "Genre", "filmes_genres_association"]
