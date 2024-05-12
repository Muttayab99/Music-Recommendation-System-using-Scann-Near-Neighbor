from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from models import db, User, Playlist, PlaylistForm, Album, Artist, Genre
from flask_login import current_user, login_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

# Define routes
@app.route('/')
def home():
    return render_template('home.html', current_user=current_user)

# Define your Flask-WTF form
class YourForm(FlaskForm):
    # Include CSRF token field
    csrf_token = HiddenField()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = YourForm()
    if request.method == 'POST':
        # Check username and password
        # If valid, login the user
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = YourForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    # Clear the session variable or cookie that tracks the user's login status
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Add routes for playlist management
@app.route('/playlists')
def playlists():
    playlists = Playlist.query.all()
    return render_template('playlist_list.html', playlists=playlists)

# Add routes for album management
@app.route('/albums')
def albums():
    albums = Album.query.all()
    return render_template('album_list.html', albums=albums)

@app.route('/album/<int:album_id>')
def album_detail(album_id):
    # Fetch album details from the database
    album = Album.query.get_or_404(album_id)
    return render_template('album_detail.html', album=album)

# Add routes for artist management
@app.route('/artists')
def artists():
    artists = Artist.query.all()
    return render_template('artist_list.html', artists=artists)

@app.route('/artist/<int:artist_id>')
def artist_detail(artist_id):
    # Fetch artist details from the database
    artist = Artist.query.get_or_404(artist_id)
    return render_template('artist_detail.html', artist=artist)

# Add routes for genre management
@app.route('/genres')
def genres():
    genres = Genre.query.all()
    return render_template('genre_list.html', genres=genres)

@app.route('/genre/<int:genre_id>')
def genre_detail(genre_id):
    # Fetch genre details from the database
    genre = Genre.query.get_or_404(genre_id)
    return render_template('genre_detail.html', genre=genre)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
