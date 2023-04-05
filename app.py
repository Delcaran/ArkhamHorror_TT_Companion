import json
import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    locations = {}

    return render_template(
        "main.html",
        locations=locations
    )


#@app.route("/monster/")
#@app.route("/monster/<name>")
#def hello_there(name:str=None):
#    return render_template(
#        "hello_there.html",
#        name=name,
#        date=datetime.now()
#    )