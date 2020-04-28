from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from myproject import app,db
from myproject.forms import RegistrationForm,LoginForm
from myproject.models import User

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/welcome')
@login_required
def welcome_user():
  return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You Have Successfully Logged Out')
  return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(form.email.data,form.username.data,form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('login'))
  return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.check_password(form.password.data):
      login_user(user)
      flash('Logged In Successfully')
      next = request.args.get('next')
      if next == None or not next[0] == '/':
        next = url_for('welcome_user')
      return redirect(next)
  return render_template('login.html',form=form)

if __name__=='__main__':
  app.run('0.0.0.0',8080,debug=True)
