#Imports
from flask import Flask
from flask import render_template
import logging





#logging 








#WEBPAGES
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

@app.route('/aboutme')
def about():
    return render_template("aboutme.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/personality')
def personality():
    return render_template("personality.html")


#error handling
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404