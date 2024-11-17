
import unittest
from flask_app.app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        """Set up test client."""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_invalid_method_for_home(self):
        """Test POST request on GET-only route."""
        # Sending a POST request to the home route which only allows GET requests
        response = self.client.post('/')  # Send a POST request to the home route
        self.assertEqual(response.status_code, 405)  # Expecting status code 405 (Method Not Allowed)

    def test_valid_method_for_home(self):
        """Test GET request on home route."""
        # Sending a GET request to the home route
        response = self.client.get('/')  # Send a GET request to the home route
        self.assertEqual(response.status_code, 200)  # Expecting status code 200 (OK)

if __name__ == '__main__':
    unittest.main()
