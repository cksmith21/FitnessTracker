from flask import Flask, render_template, url_for
from flask_login import current_user, login_required 
from models import User
from fitness_app import lm, app

@lm.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'