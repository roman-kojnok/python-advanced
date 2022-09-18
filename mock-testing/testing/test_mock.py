#!/usr/bin/python
# from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
       def test_football(self):
        with requests_mock.Mocker() as g:
            g.get('http://api:5000/get/number', text='1')
            g.get('http://api:5000/get/letter', text='a')

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)


class TestResponse2(TestBase):
    def test_Badminton(self):
        with requests_mock.Mocker() as g:
            g.get('http://api:5000/get/number', text='1')
            g.get('http://api:5000/get/letter', text='b')

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Badminton', response.data)


class TestResponse3(TestBase):
    def test_Hockey(self):
        with requests_mock.Mocker() as g:
            g.get('http://api:5000/get/number', text='1')
            g.get('http://api:5000/get/letter', text='c')

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Hockey', response.data)


class TestResponse4(TestBase):
    def test_Boxing(self):
        with requests_mock.Mocker() as g:
            g.get('http://api:5000/get/number', text='1')
            g.get('http://api:5000/get/letter', text='d')

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Boxing', response.data)


"""    def test_football(self):
        # We will mock a response of 1 and test that we get football returned.
        with patch('requests.get') as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)"""

# pytest --cov=application --cov-report=term-missing

