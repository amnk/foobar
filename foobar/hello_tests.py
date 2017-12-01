import skael
import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        skael.app.testing = True
        self.app = skael.app.test_client()

    def tearDown(self):
        pass

    def test_hello_world(self):
        rv = self.app.get('/hello')
        assert b'Hello this big awesome new World!' in rv.data

if __name__ == '__main__':
    unittest.main()
