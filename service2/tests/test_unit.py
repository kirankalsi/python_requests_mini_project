from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimals(TestBase):
    def test_animal(self):
        animals = [b'Dog', b'Cat', b'Lion', b'Cow', b'Sheep', b'Donkey', b'Duck']
        response = self.client.get(url_for('animal'))
        self.assertIn(response.data, animals)

    def test_sound_dog(self):
        response = self.client.post(
            url_for('sound'),
            data='Dog',
            follow_redirects=True
        )
        self.assertIn(b'Woof', response.data)

    def test_sound_cat(self):
        response = self.client.post(
            url_for('sound'),
            data='Cat',
            follow_redirects=True
        )
        self.assertIn(b'Meow', response.data)

    def test_sound_lion(self):
        response = self.client.post(
            url_for('sound'),
            data='Lion',
            follow_redirects=True
        )
        self.assertIn(b'Roar', response.data)

    def test_sound_cow(self):
        response = self.client.post(
            url_for('sound'),
            data='Cow',
            follow_redirects=True
        )
        self.assertIn(b'Moo', response.data)

    def test_sound_sheep(self):
        response = self.client.post(
            url_for('sound'),
            data='Sheep',
            follow_redirects=True
        )
        self.assertIn(b'Baa', response.data)

    def test_sound_donkey(self):
        response = self.client.post(
            url_for('sound'),
            data='Donkey',
            follow_redirects=True
        )
        self.assertIn(b'Hee-Haw', response.data)

    def test_sound_duck(self):
        response = self.client.post(
            url_for('sound'),
            data='Duck',
            follow_redirects=True
        )
        self.assertIn(b'Quack', response.data)