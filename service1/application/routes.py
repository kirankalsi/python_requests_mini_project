from flask import render_template, redirect, url_for, request
import requests

from application import app

@app.route('/', methods=['GET'])
def index():
    animal = requests.get("http://localhost:5001/animal")
    sound = requests.post("http://localhost:5001/sound", data=animal.text)
    return render_template('index.html', animal=animal.text, sound=sound.text)
    #sound = requests.post("http://localhost:5000/sound", data=animal.json)
    #return render_template('index.html', animal=animal.json, sound=sound.json)
