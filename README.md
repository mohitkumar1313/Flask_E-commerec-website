Assignment 02: E-Commerce Flask Application

Objective: In this assignment, you will create a Flask web application with two routes:
• a homepage (/) and,
• a products page (/products).

The application will connect to a MongoDB Atlas database to fetch and display product
information, which includes a product’s name, tag, price, and image path (local to the
Flask app). You will use Jinja2 templates to create dynamic content and Bootstrap for
styling the product page


Recent changes: 

## Unit Tests Documentation

This project includes unit tests for Flask routes and MongoDB operations.

### CI/CD Pipeline
The tests are automatically executed by GitHub Actions on each push to the `main` branch or a pull request. This ensures that the code is verified continuously for correctness.

### MongoDB Configuration
To run the tests that interact with MongoDB, ensure the following environment variables are configured in GitHub Actions as secrets:
- `MONGODB_USERNAME`
- `MONGODB_PASSWORD`

### Test Files
- **`test_routes.py`**: Contains tests for Flask routes.
- **test_database.py**: Includes reading (pinging the database) and writing (inserting documents) to MongoDB.

The tests can be triggered by any push to the main branch or pull requests.
