from pymongo import MongoClient

# MongoDB connection string
client = MongoClient('mongodb+srv://root:5mE3VQTCjz974Ftu@cluster0.mrzjz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['shop_db']
products_collection = db['products']

# Product data to insert
products = [
    {
        'name': 'Laptops',
        'tag': '20% discount',
        'price': '29.99',
        'image_path': 'images/laptop.png',
        'discount': 20  # 20% discount
    },
    {
        'name': 'Camera',
        'tag': 'Limited Edition',
        'price': '39.99',
        'image_path': 'images/camera.png',
        'discount': 0  # No discount
    },
    {
        'name': 'Mobile Phones',
        'tag': '10% discount on new arrival',
        'price': '19.99',
        'image_path': 'images/mobile.png',
        'discount': 10  # 10% discount
    },

    {
        'name': 'Laptops',
        'tag': '10% discount on new arrival',
        'price': '1109.99',
        'image_path': 'images/laptop.png',
        'discount': 40  # 10% discount
    }
]



# Clear existing products
products_collection.delete_many({})  # Remove all existing products

# Insert the products into MongoDB
products_collection.insert_many(products)
print("Products inserted successfully!")
