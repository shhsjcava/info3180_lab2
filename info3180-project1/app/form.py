from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MyForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    sex = SelectField('Select Gender', choices =[('m', 'Male'), ('f','Female')])
    email = StringField('Email Address', validators=[DataRequired()])
    address = StringField('Location' , validators =[DataRequired()])
    bio= StringField('Biography' , validators =[DataRequired()])
    photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png','Images only!'])])
    