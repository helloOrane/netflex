from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
# initialize the app with the extension
db = SQLAlchemy(app)


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
        

# create the tables
with app.app_context():
    db.create_all()