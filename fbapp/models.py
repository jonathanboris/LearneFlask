
from .views import app
from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

# Create database connection object
db = SQLAlchemy(app)


class Gender(enum.Enum):
    MALE = 0
    FEMALE = 1
    OTHER = 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender
        


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content(description='test', genger=Gender['MALE']))
    db.session.add(Content(description='test', gender=Gender['MALE']))

    db.session.commit()
    lg.warning('Database initialized')
