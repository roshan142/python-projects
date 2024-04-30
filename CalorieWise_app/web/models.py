from . import db
from flask_login import UserMixin

class User_Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    calorie = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    fats = db.Column(db.Integer)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    data = db.relationship('User_Data')

log_food = db.Table('log_food',
    db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_key=True),
)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    @property
    def calories(self):
        return (self.proteins * 4) + (self.carbs * 4) + (self.fats * 9)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    foods = db.relationship('Food', secondary=log_food, lazy='dynamic')
