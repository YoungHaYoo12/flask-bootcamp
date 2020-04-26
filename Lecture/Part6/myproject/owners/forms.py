# forms.py
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField,IntegerField

class AddForm(FlaskForm):
  owner_name = StringField('Name of Owner: ')
  puppy_id = IntegerField('ID of Puppy: ')
  submit = SubmitField('Register Owner')