from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('basic.html')

@app.route('/information')
def info():
  return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
  return "<h1>This is a page for {}</h1>".format(name.upper())

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
  pupname = ''

  if name[-1] == 'y':
    pupname = name[:-1] + 'iful'
  else:
    pupname = name + 'y'
  
  return "<h1>Your puppy latin name is: {}</h1>".format(pupname)

@app.route('/home')
def home():
  return render_template('home.html')

if __name__ == '__main__':
  app.run('0.0.0.0',8080, debug=True)