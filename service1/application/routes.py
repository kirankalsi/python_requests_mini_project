from flask import render_template, redirect, url_for, request

from application import app

@app.route('/')
def index():
    return render_template('index.html')
