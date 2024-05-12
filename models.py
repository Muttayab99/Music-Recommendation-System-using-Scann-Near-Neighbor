from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_enabled = db.Column(db.Boolean, default=True)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return self.is_enabled

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class PlaylistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Create Playlist')

# Define the Album model
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    release_date = db.Column(db.Date)
    # Define other fields for the Album model as needed

# Define the Artist model
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    # Define other fields for the Artist model as needed

# Define the Genre model
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Define other fields for the Genre model as needed
