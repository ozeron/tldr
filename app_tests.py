import os
import app
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'Hello, World!' in rv.data

if __name__ == '__main__':
    unittest.main()
