from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,TextField,TextAreaField
from wtforms.validators import DataRequired, Email

images = ["png","jpg"]
class ProfileForm(FlaskForm):
    firstname = StringField('FName', validators=[DataRequired()])
    lastname = StringField('LName', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    biography = TextAreaField('Message', validators=[DataRequired()])
    photo = FileField('photo', validators=[ FileRequired(),
        FileAllowed(images, 'Images only!')])