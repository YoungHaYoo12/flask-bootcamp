from flask import redirect, render_template,url_for,flash,request,abort
from myproject import app, db
from myproject.models import User
from myproject.forms import LoginForm,RegistrationForm
from flask_login import login_user,logout_user,login_required

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
  return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You Have Been Logged Out')
  return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    email = form.email.data
    password = form.password.data
    user = User.query.filter_by(email=email).first()
    if user is not None and user.check_password(password):
      login_user(user)
      flash('You Have Been Logged In')
      next = request.args.get('next')
      if next == None or not next[0] == '/':
        next = url_for('welcome_user')
      return redirect(next)
  return render_template('login.html',form=form)
      
    

@app.route('/register',methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    email = form.email.data
    username = form.username.data
    password = form.password.data
    new_user = User(email,username,password)
    db.session.add(new_user)
    db.session.commit()
    flash('Thanks for Registering')
    return redirect(url_for('login'))
  return render_template('register.html',form=form)

if __name__ == '__main__':
  app.run('0.0.0.0',8080,debug=True)