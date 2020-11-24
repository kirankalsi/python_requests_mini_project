from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_homepage(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_animal(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "Lion"
                p.return_value.text = "Roar"

                response = self.client.get(url_for('index'))
                self.assertIn(b'Your animal is: Lion', response.data)
                self.assertIn(b'It makes this sound: Roar', response.data)
                self.assertEqual(response.status_code, 200)