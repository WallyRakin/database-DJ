from flask import Flask, jsonify, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, Playlist_Song
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm, NewSongForPlaylistForm2
from sqlalchemy import not_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:pass@localhost/playlist-app'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template("playlist.html", playlist=playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    form = PlaylistForm()
    if form.validate_on_submit():
        new_playlist = Playlist.new_playlist(
            form.name.data, form.description.data)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_playlist.html', form=form)


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    song = Song.query.get_or_404(int(song_id))
    return render_template("song.html", song=song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    form = SongForm()
    if form.validate_on_submit():
        new_song = Song.new_song(
            form.title.data, form.artist.data)
        db.session.add(new_song)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_song.html', form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS
    all_songs = Song.query.all()
    playlist = Playlist.query.get_or_404(playlist_id)

    # Restrict form to songs not already on this playlist
    current_songs = [song.id for song in playlist.songs]
    available_songs = [
        song for song in all_songs if song.id not in current_songs
    ]

    # #####

    form = NewSongForPlaylistForm()
    forms = {s.id: form for s in all_songs}
    if form.validate_on_submit():
        try:
            new_song = int(form.id.data)
            print(new_song)
            playlist_song = Playlist_Song(
                playlist_id=playlist_id, song_id=new_song)
            print(type(playlist_song.playlist_id), type(playlist_song.song_id))
            db.session.add(playlist_song)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error:", e)
            return "fail"
        else:
            return "success"
    else:
        print(form.errors)

    # #####

    return render_template("add_song_to_playlist(test).html", playlist=playlist, forms=forms, all_songs={song.id: {"title": song.title, "artist": song.artist} for song in all_songs}, current_songs=current_songs, available_songs=available_songs, form=form)


@app.route("/playlists/<int:playlist_id>/add-song2", methods=["GET", "POST"])
def add_song_to_playlist2(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS
    all_songs = Song.query.all()
    playlist = Playlist.query.get_or_404(playlist_id)

    # Restrict form to songs not already on this playlist
    current_songs = [song.id for song in playlist.songs]
    available_songs = [
        (song.id, f'"{song.title}" by:{song.artist}') for song in all_songs if song.id not in current_songs
    ]
    print("current song:", available_songs)

    #####
    form = NewSongForPlaylistForm2()

    form.song_id.choices = available_songs

    if form.validate_on_submit():
        try:
            new_song = form.song_id.data
            playlist_song = Playlist_Song(
                playlist_id=playlist_id, song_id=new_song)
            db.session.add(playlist_song)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return redirect(f"/playlists/{playlist_id}/add-song2")
        else:
            return redirect(f"/playlists/{playlist_id}")
    else:
        print(form.errors)
        # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    print(playlist.songs)
    return render_template("add_song_to_playlist.html",
                           playlist=playlist,
                           form=form)


@app.route("/songs/info", methods=["GET"])
def get_playlist_info():
    song_info = db.session.query(Song.id, Song.title).all()
    db.session.close()
    return jsonify([{"id": song.id, "title": song.title} for song in song_info])


app.run(debug=True)
