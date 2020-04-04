from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from os.path import join, dirname, realpath

app = Flask(__name__)
#app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://sutkdnkjmzucrd:dd0f28e117aeaa510f57d36d180f78e20d10724b4754662f307faf132cbbe840@ec2-52-87-58-157.compute-1.amazonaws.com:5432/dcq5sp3v71dd68"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

#Uploads Folder
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads')

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
