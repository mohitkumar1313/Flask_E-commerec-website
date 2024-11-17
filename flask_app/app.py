from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the app here
app = Flask(__name__)

# MongoDB credentials
db_username = os.environ["MONGODB_USERNAME"]
db_password = os.environ["MONGODB_PASSWORD"]

# MongoDB Atlas connection
client = MongoClient(f'mongodb+srv://{db_username}:{db_password}@cluster0.mrzjz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['shop_db']
products_collection = db['products']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = list(products_collection.find())  # Convert cursor to list
    for product in products:
        product['discount'] = float(product['discount']) if isinstance(product['discount'], str) else product['discount']
    return render_template('products.html', products=products)

@app.route('/upload_product', methods=['GET', 'POST'])
def upload_product():
    if request.method == 'POST':
        name = request.form['name']
        tag = request.form['tag']
        price = float(request.form['price'])  # Ensure price is a float
        discount = float(request.form['discount'])  # Ensure discount is a float
        image = request.files['image']

        # Define the images directory
        image_dir = 'static/images'

        # Create the images directory if it doesn't exist
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        if image and image.filename != '':
            # Define the image path
            image_path = os.path.join(image_dir, image.filename)

            try:
                # Save the image to the specified path
                image.save(image_path)

                # Debug output to confirm saving
                print(f"Image saved at: {image_path}")

                # Create a product document
                product = {
                    'name': name,
                    'tag': tag,
                    'price': price,
                    'image_path': f'images/{image.filename}',  # Store the relative path for MongoDB
                    'discount': discount
                }

                # Insert the product into MongoDB
                products_collection.insert_one(product)

                return redirect(url_for('products'))  # Redirect to the products page
            except Exception as e:
                return f"Failed to upload image or save product: {e}", 500  # Error response

    return render_template('upload_product.html')

if __name__ == '__main__':
    app.run(debug=True)
