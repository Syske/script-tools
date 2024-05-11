from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/index") 
def index(name=None):
    return render_template('index.html', name=name)