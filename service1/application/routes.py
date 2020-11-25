from flask import Flask, render_template, redirect, url_for, request
import requests

from application import app

#app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    try:
        animal = requests.get("http://service2:5001/animal")
        sound = requests.post("http://service2:5001/sound", data=animal.text)
        return render_template('index.html', animal=animal.text, sound=sound.text)
    except requests.exceptions.RequestException:
        return render_template('error.html')
    #sound = requests.post("http://localhost:5000/sound", data=animal.json)
    #return render_template('index.html', animal=animal.json, sound=sound.json)
