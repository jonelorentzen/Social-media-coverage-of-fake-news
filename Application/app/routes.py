from flask import render_template, flash, redirect, url_for, request
from app import app, query_user, query_comments, query_friends, query_posts, query_post, insert_user, insert_post, insert_comment, insert_friend, update_user
from app.forms import IndexForm, PostForm, FriendsForm, ProfileForm, CommentsForm
from datetime import datetime
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, logout_user, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app import User
import os

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["20 per minute", "5 per second"],
)

ALLOWED_EXTENSIONS = set(['apng','bmp','gif','ico','cur','jpg','jpeg','jfif','pjp','png','svg','tif','tiff','webp','pjpeg'])
# Allowed extensions is defined with the HTML Embeded Image element tag in mind.

#To avoid storing files in a place unintended
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# home page/login/registration
@limiter.limit("100/day;10/hour;7/minute", methods=['POST'])
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('stream'))
    #Retrieves form and performes login / register process
    form = IndexForm()

    if form.login.validate_on_submit():
        loginattempt = query_user(form.login.username.data)
        if loginattempt is None:
            flash('Sorry, incorrect credentials!')
        else:
            user = User(loginattempt['id'], loginattempt)

            if user.data is None:
                flash('Sorry, incorrect credentials!')
            elif check_password_hash(user.data['password'], form.login.password.data):
                login_user(user, remember=form.login.remember_me.data)
                return redirect(url_for('stream'))
            else:
                flash('Sorry, incorrect credentials!', "warning")

    elif form.register.validate_on_submit():
        flash(f"Account created for {form.register.username.data}!", "success")
        insert_user(form.register.username.data, form.register.first_name.data, form.register.last_name.data, form.register.password.data)
        return redirect(url_for('index'))

    return render_template('index.html', title='Welcome', form=form)


# content stream page
@app.route('/stream', methods=['GET', 'POST'])
@limiter.limit("100/day;10/hour;7/minute", methods=['POST'])
@login_required
def stream():
    form = PostForm()
    if form.validate_on_submit():

        #Check and verifies filename
        if form.image.data:
            file = form.image.data
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_PATH'], filename)
                form.image.data.save(path)
            else:
                flash('Invalid Filetype', "warning")
                return redirect(url_for('stream'))

        insert_post(current_user.data['id'], form.content.data, form.image.data.filename)
        return redirect(url_for('stream'))

    posts = query_posts(current_user.data['id'])
    return render_template('stream.html', title='Stream', form=form, posts=posts)

# comment page for a given post and user.
@app.route('/comments/<int:p_id>', methods=['GET', 'POST'])
@login_required
def comments(p_id):
    form = CommentsForm()
    if form.validate_on_submit():
        user = query_user(current_user.data['username'])
        insert_comment(p_id, user['id'], form.comment.data)
        flash("Comment posted!", "success")

    post = query_post(p_id)
    all_comments = query_comments(p_id)
    return render_template('comments.html', title='Comments', username=current_user.data['username'], form=form, post=post, comments=all_comments)

# page for seeing and adding friends
@app.route('/friends', methods=['GET', 'POST'])
@limiter.limit("400/day;100/hour;10/minute", methods=['POST'])
@login_required
def friends():
    # if current_user.data['username'] != username:
    #   return redirect(url_for('friends', username=current_user.data['username']))
    form = FriendsForm()
    #user = query_db('SELECT * FROM Users WHERE username="{}";'.format(username), one=True)
    if form.validate_on_submit():
        friend = query_user(form.username.data)
        if friend is None:
            flash('User does not exist', "error")
        else:
            insert_friend(current_user.data['id'], friend['id'])
    
    all_friends = query_friends(current_user.data['id'])
    return render_template('friends.html', title='Friends', username=current_user.data['username'], friends=all_friends, form=form)

# see and edit detailed profile information of a user
@app.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    form = ProfileForm()
    if current_user.data['username'] == username:
        if form.validate_on_submit():
            update_user(form.education.data, form.employment.data, form.music.data, form.movie.data, form.nationality.data, form.birthday.data, username)
            return redirect(url_for('profile', username=username))
    
    user = query_user(username)
    return render_template('profile.html', title='profile', username=username, user=user, form=form)


@app.route('/logout')
@login_required
def logout():
        logout_user()
        flash("Successfully logged out", "success")
        return redirect(url_for('index'))
