from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from init import db


class Base(DeclarativeBase):
    pass

class Movie(db.Model):

    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250))
    release_year: Mapped[int] = mapped_column(Integer)
    picture: Mapped[str] = mapped_column(String(250))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"))
    video: Mapped[str] = mapped_column(String(250))
    director: Mapped[str] = mapped_column(String(250))
    resume: Mapped[str] = mapped_column(String(650))

    def __repr__(self):
        return f"<Movie(name={self.name}, release_year={self.release_year})>"

class TvShow(db.Model):

    __tablename__ = "tv-show"


    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250))
    release_year: Mapped[int] = mapped_column(Integer)
    picture: Mapped[str] = mapped_column(String(250))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"))
    video: Mapped[str] = mapped_column(String(250))
    director: Mapped[str] = mapped_column(String(250))
    resume: Mapped[str] = mapped_column(String(650))
    seasons_count: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"<TvShow(name={self.name}, release_year={self.release_year})>"
    
class Genre(db.Model):

    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))

    def __repr__(self):
        return f"<Genre(name={self.name})>"
    
class Person(db.Model):
    
        __tablename__ = "person"
    
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(60))
    
        def __repr__(self):
            return f"<Person(name={self.name})>"
        
# db = SQLAlchemy(model_class=Base)