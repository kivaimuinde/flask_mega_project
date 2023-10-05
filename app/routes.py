from app import app


@app.route("/")
@app.route("/index")
def index():
    return "This is index page"


@app.route("/hello")
def hello():
    return "THis is hello page"


@app.route("/greeting")
def greeting():
    return "This is greetings page"


@app.route("/message")
def message():
    return "This is message page"
    
