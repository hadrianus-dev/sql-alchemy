# pylint: disable=C0301
# pylint: disable=E0239
from sqlalchemy import Column, Integer, String
from infra.config.base import Base

class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(255))
    genre = Column(String(255))
    year = Column(Integer)

    def __repr__(self):
        return f"Film [id={self.id}, title={self.title}, description={self.description}, genre={self.genre}, year={self.year}]"
