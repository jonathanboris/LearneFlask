from flask import Flask

from .views import app
from . import models

# Connect sqlalchemy to app
# models.db.app = app
# models.db.init_app(app)
# with app.app_context():
#     models.db.create_all()


@app.cli.command()
def init_db():
    models.init_db()
