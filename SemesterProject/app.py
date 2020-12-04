from flask import Flask
from flask import render_template
import jinja2


app = Flask(__name__)


@app.route('/')
def index():

    return render_template("index.html")
    

@app.route('/elements')
def elements():
    return render_template("elements.html")

@app.route('/generic')
def generic():
    return render_template("generic.html")

@app.route('/lab10')
def ten():
    return render_template("lab10.html")