from flask import render_template
from app import app

user = {'username': 'John'}
@app.route("/")
@app.route("/index")
def index():
    
    title="Home"
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title=title, user=user , posts=posts)


@app.route("/hello")
def hello():
    message = {'message': 'Hello'}
    return render_template("hello.html", message=message,user=user )


@app.route("/greetings")
def greeting():
    greeting = {'greeting': 'Welcome'}
    return  render_template("greetings.html", greeting=greeting,user=user )


@app.route("/messages")
def message():
    message = {'message': 'Welcome to Microblog'}
    return render_template("message.html", message=message,user=user )
    
