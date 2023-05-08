
from .views import app
from flask_sqlalchemy import SQLAlchemy
import logging as lg

# Create database connection object
db = SQLAlchemy(app)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Integer(), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content(description='test', gender=1))
    db.session.add(Content(description='test', gender=2))

    db.session.commit()
    lg.warning('Database initialized')
