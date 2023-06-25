from datetime import datetime
from hashlib import md5
from os import EX_TEMPFAIL
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from fitness_app import db

class User(db.Model, UserMixin): 

    '''
        id -> Integer, primary key, unique
        username -> String, 120 characters, unique
        email -> String, 120 characters, unique  
        password_hash -> String, 80 characters 
    '''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(80))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def __init__(self, username, email, password):
        self.username = username
        self.email = email 
        self.set_password(password)