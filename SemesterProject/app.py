from flask import Flask
from flask import render_template
import logging



app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    app.logger.info("This is my page that is under construction")
    return render_template("index.html")
    

@app.route('/hello')
def hello_world():
    app.logger.warning("How is it even possible you could break my website when it isn't even live yet?")
    return 'Hello, World!'
