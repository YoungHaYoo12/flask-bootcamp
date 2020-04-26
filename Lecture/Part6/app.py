from myproject import app 
from flask import render_template

@app.route('/')
def index():
  return render_template('home.html')

if __name__ == '__main__':
  app.run('0.0.0.0',8080,debug=True)