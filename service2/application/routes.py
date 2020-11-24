from flask import Flask, Response, request, jsonify
import random

from application import app

@app.route('/animal', methods=['GET'])
def animal():
    animals = ['Dog', 'Cat', 'Lion', 'Cow', 'Sheep', 'Donkey', 'Duck']
    animal = random.choice(animals)
    return Response(animal, mimetype='text/plain')
    #return jsonify(animal)

@app.route('/sound', methods=['POST'])
def sound():
    #data_sent = request.get_json()
    data_sent = request.data.decode('utf-8')
    #sounds = {'Dog':'Woof', 'Cat':'Meow', 'Lion':'Roar', 'Cow':'Moo', 'Sheep':'Baa', 'Donkey':'Hee-Haw', 'Duck':'Quack'}
    #sound = sounds[data_sent]
    if data_sent == 'Dog':
        sound = 'Woof'
    elif data_sent == 'Cat':
        sound = 'Meow'
    elif data_sent == 'Lion':
        sound = 'Roar'
    elif data_sent == 'Cow':
        sound = 'Moo'
    elif data_sent == 'Sheep':
        sound = 'Baa'
    elif data_sent == 'Donkey':
        sound = 'Hee-Haw'
    else:
        sound = 'Quack'
    return Response(sound, mimetype='text/plain')
    #return jsonify(sound)