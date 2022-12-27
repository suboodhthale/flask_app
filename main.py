"""to run flask application:
1.type in terminal:-> flask app main run   (where main is file name we want to run)
2. to run on specified port use-> flask app main run --port 8080
3. to publish ur application on public IP:-> flask app main run --port 8080 --host 0.0.0.0"""
from flask import Flask

app = Flask(__name__)
@app.route("/")            #We use flask.app decorator to tell flask about relative url
def hello_world():
    return "<p>Hello World</p>"
@app.route("/details")
def details():
    return "<p> This is route to details </p>"
