"""Models for Playlist app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'Playlists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    songs = db.relationship(
        'Song', secondary='Playlists_Song', backref='playlists')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def new_playlist(cls, name, description):
        return cls(name, description)


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'Songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(50), nullable=False)

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    @classmethod
    def new_song(cls, title, artist):
        return cls(title, artist)


class Playlist_Song(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'Playlists_Song'
    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'Playlists.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey(
        'Songs.id'), primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


# if __name__ == "__main__":
#     from app import app
#     with app.app_context():
#         db.drop_all()
#         db.create_all()
