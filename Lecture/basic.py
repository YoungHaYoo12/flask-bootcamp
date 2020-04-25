from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('basic.html')

@app.route('/puppy/<name>')
def puppy(name):
  return "<h1>This is a page for {}</h1>".format(name.upper())

@app.route('/home')
def home():
  return render_template('home.html')

if __name__ == '__main__':
  app.run('0.0.0.0',8080, debug=True)