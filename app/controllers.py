# Import flask dependencies
from flask import Blueprint, request, render_template

# UNUSED NOW: Import the database object from the main app module
# from app import db

# Define the blueprint: 'auth', set its url prefix: app.url/auth
routes = Blueprint('routes', __name__)


@routes.route('/')
def homepage():
    return render_template('homepage.html')


@routes.route('/login/')
def login():
    return render_template('login.html')


@routes.route('/signup/')
def signup():
    return render_template('signup.html')


@routes.route('/courses/')
def courses():
    return render_template('courses.html')


@routes.route('/about/')
def about():
    return render_template('about.html')
