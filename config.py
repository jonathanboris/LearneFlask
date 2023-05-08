import os
FB_APP_ID = 749129683562465

SECRET_KEY = "Q6!\"LNQ^i3(C]VZe j2D'Xap"

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
