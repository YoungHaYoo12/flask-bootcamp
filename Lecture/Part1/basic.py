from flask import (Flask, render_template, request,session,redirect,url_for)
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,RadioField,SelectField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
  breed = StringField('What breed are you?', validators=[DataRequired()])
  neutered = BooleanField('Have you been neutered?')
  mood = RadioField('Please choose your mood:', choices=[('mood_one','Happy'),('mood_two','Excited')])
  food_choice = SelectField('Pick your favorite food:',choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
  feedback = TextAreaField()
  submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
  form = InfoForm()
  if form.validate_on_submit():
    session['breed'] = form.breed.data
    session['neutered'] = form.neutered.data
    session['mood'] = form.mood.data
    session['food'] = form.food_choice.data
    session['feedback'] = form.feedback.data

    return redirect(url_for('thank_you'))


  return render_template('index.html',form=form)

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
  first = request.args.get('first')
  last = request.args.get('last')

  return render_template('thank_you.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html')

if __name__ == '__main__':
  app.run('0.0.0.0',8080, debug=True)