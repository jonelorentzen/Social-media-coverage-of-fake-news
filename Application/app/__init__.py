from flask import Flask, g
from config import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime
import sqlite3
import os

# create and configure app
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)

# TODO: Handle login management better, maybe with flask_login?
login_manager = LoginManager(app)

# get an instance of the db
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db

# initialize db for the first time
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# perform generic query, not very secure yet
def query_db(query, one=False):
    db = get_db()
    cursor = db.execute(query)
    rv = cursor.fetchall()
    cursor.close()
    db.commit()
    return (rv[0] if rv else None) if one else rv

# TODO: Add more specific queries to simplify code


def query_user(username):
    return query_db('SELECT * FROM Users WHERE username="{}";'.format(username), one=True)

def query_posts(u_id):
    return query_db('SELECT p.*, u.*, (SELECT COUNT(*) FROM Comments WHERE p_id=p.id) AS cc FROM Posts AS p JOIN Users'
                    ' AS u ON u.id=p.u_id WHERE p.u_id IN (SELECT u_id FROM Friends WHERE f_id={0}) OR p.u_id IN (SELECT'
                    ' f_id FROM Friends WHERE u_id={0}) OR p.u_id={0} ORDER BY p.creation_time DESC;'.format(u_id))

def query_post(p_id):
    return query_db('SELECT * FROM Posts WHERE id={};'.format(p_id), one=True)

def query_comments(p_id):
    return query_db('SELECT DISTINCT * FROM Comments AS c JOIN Users AS u ON c.u_id=u.id WHERE c.p_id={} ORDER BY c.creation_time DESC;'.format(p_id))

def query_friends(u_id):
    return query_db('SELECT * FROM Friends AS f JOIN Users as u ON f.f_id=u.id WHERE f.u_id={} AND f.f_id!={} ;'.format(u_id, u_id))

def insert_user(username, firstname, lastname, password):
    query_db('INSERT INTO Users (username, first_name, last_name, password) VALUES("{}", "{}", "{}", "{}");'.format(
        username, firstname, lastname, generate_password_hash(password, 'sha256')))

def insert_post(u_id, content, filename):
    query_db('INSERT INTO Posts (u_id, content, image, creation_time) VALUES({}, "{}", "{}", \'{}\');'.format(
        u_id, content, filename, datetime.now()))

def insert_comment(p_id, u_id, comment):
    query_db('INSERT INTO Comments (p_id, u_id, comment, creation_time) VALUES({}, {}, "{}", \'{}\');'.format(p_id, u_id, comment, datetime.now()))

def insert_friend(u_id, f_id):
    query_db('INSERT INTO Friends (u_id, f_id) VALUES({}, {});'.format(u_id, f_id))

def update_user(education, employment, music, movie, nationality, birthday, username):
    query_db('UPDATE Users SET education="{}", employment="{}", music="{}", movie="{}", nationality="{}",'
             ' birthday=\'{}\' WHERE username="{}" ;'.format(education, employment, music, movie, nationality, birthday, username))

# automatically called when application is closed, and closes db connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# initialize db if it does not exist
if not os.path.exists(app.config['DATABASE']):
    init_db()

if not os.path.exists(app.config['UPLOAD_PATH']):
    os.mkdir(app.config['UPLOAD_PATH'])

#load user function for login manager
@login_manager.user_loader
def load_user(user_id):

    return User(user_id, query_db('SELECT * FROM Users WHERE id="{}";'.format(user_id), one=True))

#user class inheriting UserMixin to user for login Manager
class User(UserMixin):
    def __init__(self, id, data):
        self.id = id
        self.data = data


from app import routes