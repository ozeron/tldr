import os
import json
import app
import unittest
import tempfile


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))


def json_request(self, url, data={}):
    return self.app.post(url,
                         data=json.dumps(data),
                         content_type='application/json')


def build_summary(client, text):
    """Records a message"""
    rv = json_request(client, '/api/summary_from_text', {'text': text})
    return rv


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_empty(self):
        rv = self.app.get('/')
        expected = {'status': 'ok'}
        self.assertEqual(json_of_response(rv), expected)

    def test_summary_build(self):
        rv = build_summary(self, 'test message 1')
        expected = {'text': 'test message 1', 'status': 'ok'}
        self.assertEqual(json_of_response(rv), expected)

    def test_empty_summary_build(self):
        rv = build_summary(self, '')
        expected = {
            'message': 'set text dict key to generate summary',
            'status': 'error'
        }
        self.assertEqual(json_of_response(rv), expected)

    def test_empty_summary_data_build(self):
        rv = json_request(self, '/api/summary_from_text')
        expected = {
            'message': 'set text dict key to generate summary',
            'status': 'error'
        }
        self.assertEqual(json_of_response(rv), expected)


if __name__ == '__main__':
    unittest.main()
