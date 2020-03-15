from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from os.path import join, dirname, realpath

app = Flask(__name__)
#app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://proj:usersdatabase@localhost/users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

#Uploads Folder
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads')

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
