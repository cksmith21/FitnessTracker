from flask import Flask
import os 
from flask import Flask, render_template, url_for, views
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .views import *
from .models import *

'''
    Creation of necessary items. Login manager, database configuration, and app initiation. 
'''

# define login manager
lm = LoginManager()

# base directory to create database
basedir = os.path.abspath(os.path.dirname(__file__))

# create Flask object
app = Flask(__name__)

# get database information
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'fitness_information.db')
db = SQLAlchemy(app)

# login manager initalization

lm.init_app(app)
lm.session_protection = "strong"
lm.login_view = "login"
lm.init_app(app)

