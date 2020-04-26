# forms.py
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField,IntegerField

class AddForm(FlaskForm):
  name = StringField('Name of Puppy: ')
  submit = SubmitField('Add Puppy')

class DeleteForm(FlaskForm):
  id = IntegerField("ID Number of Puppy to Remove: ")
  submit = SubmitField('Remove Puppy')

class OwnerForm(FlaskForm):
  owner_name = StringField('Name of Owner: ')
  puppy_id = IntegerField('ID of Puppy: ')
  submit = SubmitField('Register Owner')