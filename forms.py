"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField('Name', validators=[DataRequired(), Length(0, 50)], render_kw={
                       "class": "form-control"})
    description = TextAreaField('Description', render_kw={
                                "class": "form-control"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-success"})


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    artist = StringField('Artist', validators=[DataRequired(), Length(0, 50)], render_kw={
        "class": "form-control"})
    title = StringField('Title', validators=[DataRequired(), Length(0, 50)], render_kw={
        "class": "form-control"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-success"})


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    id = HiddenField(default='')


class NewSongForPlaylistForm2(FlaskForm):
    """Form for adding a song to playlist."""
    song_id = SelectField('Song', choices=[], validators=[DataRequired()], render_kw={
                          "class": "",
                          "placeholder": "Search here..."})
