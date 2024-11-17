import os
import unittest
from pymongo import MongoClient
from flask_app.app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        """Set up test client."""
        self.client = app.test_client()  # Create a test client for Flask
        app.config['TESTING'] = True  # Enable testing mode in Flask

    def test_mongo_connection(self):
        """Test MongoDB read operation by pinging the database."""
        client = MongoClient(f'mongodb+srv://{os.environ["MONGODB_USERNAME"]}:{os.environ["MONGODB_PASSWORD"]}@cluster0.mrzjz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Use the correct MongoDB URI
        db = client['shop_db']

        # Ping the MongoDB server
        try:
            db.command('ping')  # Ping command to verify connection
            mongo_connected = True
        except Exception as e:
            mongo_connected = False

        # Assert that MongoDB is connected successfully
        self.assertTrue(mongo_connected)

        # Ensure the client is closed after test
        client.close()

    def test_write_data_to_db(self):
        """Test MongoDB write operation by inserting multiple documents."""
        client = MongoClient(
            f'mongodb+srv://{os.environ["MONGODB_USERNAME"]}:{os.environ["MONGODB_PASSWORD"]}@cluster0.mrzjz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client['shop_db']
        collection = db['products']

        # Insert multiple new data into the collection
        new_data = [
            {
                "name": "Test Product-1",
                "tag": "Test Tag",
                "price": 19.99,
                "image_path": "images/laptop.png",
                "discount": 10.0
            },
            {
                "name": "Test Product-2",
                "tag": "Test Tag",
                "price": 19.99,
                "image_path": "images/laptop.png",
                "discount": 15.0
            }
        ]

        # Insert multiple records
        collection.insert_many(new_data)

        # Query the database to check if the data is inserted
        inserted_data_1 = collection.find_one({"name": "Test Product-1"})
        inserted_data_2 = collection.find_one({"name": "Test Product-2"})

        # Assert that the data is not None and matches the inserted values
        self.assertIsNotNone(inserted_data_1)  # Check that the first data is inserted
        self.assertEqual(inserted_data_1['name'], 'Test Product-1')  # Verify the first product data

        self.assertIsNotNone(inserted_data_2)  # Check that the second data is inserted
        self.assertEqual(inserted_data_2['name'], 'Test Product-2')  # Verify the second product data

        # Ensure the client is closed after test
        client.close()

if __name__ == '__main__':
    unittest.main()
