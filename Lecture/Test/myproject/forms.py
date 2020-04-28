from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from myproject.models import User

class RegistrationForm(FlaskForm):
  email = StringField('Email:',validators=[DataRequired(),Email()])
  username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password:',validators=[DataRequired(),EqualTo('pass_confirm',"Passwords Must Match")])
  pass_confirm = PasswordField('Confirm Password:',validators=[DataRequired()])
  submit = SubmitField('Register')

  def check_email(self,field):
    if User.query.filter_by(email=field.data).first():
      raise ValidationError('Account Associated with That Email Already Exists')
  
  def check_username(self,field):
    if User.query.filter_by(username=field.data).first():
      raise ValidationError('Username Already Taken')

class LoginForm(FlaskForm):
  email = StringField('Email:',validators=[DataRequired(),Email()])
  password = PasswordField('Password:',validators=[DataRequired()])
  submit = SubmitField('Log In')