# Assignment 02: E-Commerce Flask Application

## Objective: In this assignment, you will create a Flask web application with two routes:
• a homepage (/) and,
• a products page (/products).

The application will connect to a MongoDB Atlas database to fetch and display product
information, which includes a product’s name, tag, price, and image path (local to the
Flask app). You will use Jinja2 templates to create dynamic content and Bootstrap for
styling the product page


# Recent changes: 

## Unit Tests Documentation
This project includes unit tests that validate the functionality of Flask routes and MongoDB operations. These tests ensure that the application behaves as expected, both for the user-facing API and interactions with the database.

## CI/CD Pipeline
The unit tests are automatically executed by GitHub Actions through the CI/CD pipeline. This automation ensures continuous testing of the application’s functionality and performance. The GitHub Actions pipeline is defined in the .github/workflows/ci.yml file. The tests are triggered on the following events:

Push: Any push to the main branch triggers the tests to run.
Pull Request: Any pull request targeting the main branch also triggers the test pipeline.
The CI/CD pipeline automates the following process:

Setup: The environment is configured, including setting up dependencies and environment variables.
Test Execution: The unit tests for Flask routes and MongoDB operations are run.
Results Reporting: The results of the tests (pass/fail) are displayed in GitHub Actions, allowing the team to see whether the tests succeeded or failed.
MongoDB Configuration
For the tests involving MongoDB operations, ensure that the following secrets are configured in GitHub Actions under the repository’s settings:

MONGODB_USERNAME: MongoDB username for authentication.
MONGODB_PASSWORD: MongoDB password for authentication.
These secrets are used to connect securely to the MongoDB database during test execution. The credentials are never exposed in the codebase, ensuring sensitive information remains secure.

## Test Files
The unit tests are organized into separate files based on functionality:

test_routes.py: Contains unit tests that validate the functionality of Flask routes. These tests ensure that the API routes return the expected status codes and content. For example, the tests verify that valid GET requests return a 200 OK response, and POST requests correctly create resources like users or products.

test_database.py: Contains unit tests for MongoDB operations. This includes tests for:

Reading: Ensures that the application can connect to the MongoDB database and query data.
Writing: Verifies that the application can insert data into the database and handle CRUD operations.
Example of a route test:

python
Copy code
def test_homepage_route(self):
    """Test the response of the homepage route."""
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Welcome to the Shop', response.data)
Example of a MongoDB test:

python
Copy code
def test_mongo_connection(self):
    """Test MongoDB connection by pinging the database."""
    client = MongoClient(f'mongodb+srv://{os.environ["MONGODB_USERNAME"]}:{os.environ["MONGODB_PASSWORD"]}@cluster0.mongodb.net')
    db = client['shop_db']
    try:
        db.command('ping')  # Ping the database to check the connection
        mongo_connected = True
    except Exception as e:
        mongo_connected = False
    self.assertTrue(mongo_connected)
    client.close()
## Test Execution
The tests are automatically triggered by any push to the main branch or any pull request targeting it. This ensures that the latest code changes are continuously tested.
