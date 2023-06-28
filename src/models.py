from datetime import datetime
from hashlib import md5
from os import EX_TEMPFAIL
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from fitness_app import db
from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType
import uuid

class User(db.Model, UserMixin): 

    __tablename__ = 'user'

    '''
        id -> Integer, primary key, unique
        username -> String, 120 characters, unique
        email -> String, 120 characters, unique  
        password_hash -> String, 80 characters 
        created_at -> time user is created at
    '''

    user_id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(80))
    created_at = db.Column(db.DateTime(timezone=True), server_default = func.now())

    def __repr__(self):
        return f'<User {self.username}'
    
    def add_user(self):
        db.session.add(self)
        db.session.commit()

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

class Workouts(db.Model):

    __tablename__ = 'workouts'

    workout_id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUIDType(binary=False), db.ForeignKey("user.user_id"))
    user = db.relationship("User", backref=db.backref("user", userlist=False))

    workout_name = db.Column(db.String(120))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    weight = db.Column(db.Double)
    units = db.Column(db.String(10))
    date = db.Column(db.DateTime(timezone=True), server_default = func.now())

    def __init__(self, workout_id, user_id, workout_name, reps, sets, weight, unit, date):
        
        self.workout_id = workout_id
        self.user_id = user_id
        self.workout_name = workout_name
        self.reps = reps
        self.sets = sets
        self.weight = weight
        self.unit = unit
        self.date = date

    def save_to_db(self):
        
        db.session.add(self)
        db.session.commit()