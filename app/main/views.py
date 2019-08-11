
#main/views.py

from flask import render_template, request, redirect, Blueprint
from app.main import main
from app.auth import auth
from app.request import get_quote
from app.models import Blog

@main.route('/')
def index():
    '''
    Homepage 

    '''

    quotes = get_quote()

    page = request.args.get('page', 1, type=int)
    posts = Blog.query.order_by(Blog.timestamp.desc()).all()
    return render_template('index.html',quotes = quotes, posts=posts)



@main.route('/info')
def info():
    '''
    Infor page
    '''
    return render_template('info.html')



# Comments.

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template("profile/profile.html", user = user, posts = posts)

