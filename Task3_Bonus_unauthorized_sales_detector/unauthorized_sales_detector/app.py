# Imports: You're importing Flask to create your web application, request to handle incoming requests, and jsonify to convert Python dictionaries to JSON responses.
from flask import Flask, request, jsonify

# App Initialization: Initializes a new Flask application.
app = Flask(__name__)

# Route Definition: Defines a route /detect-unauthorized-sales that accepts POST requests. This is where clients will send data to be processed.
@app.route('/detect-unauthorized-sales', methods=['POST'])

# Function and Data Extraction: Defines the function detect_unauthorized_sales to handle requests to the route. It attempts to parse the JSON data from the incoming request.
def detect_unauthorized_sales():
    data = request.get_json()
    
    # Input Validation: Checks if the received data is valid and contains the required keys (productListings and salesTransactions). If not, it returns a 400 Bad Request error with a descriptive message.
    if not data or 'productListings' not in data or 'salesTransactions' not in data:
        return jsonify({'error': 'Bad request, missing data'}), 400
    
    # Authorized Sellers Mapping: Creates a dictionary (authorized_sellers) mapping each product ID to its authorized seller ID from the productListings provided in the request.
    authorized_sellers = {item['productID']: item['authorizedSellerID'] for item in data['productListings']}
    
    # Unauthorized Sales List: Initializes a list to store unauthorized sales transactions.
    unauthorized_sales = []

    # Detection Logic: Iterates over each transaction in salesTransactions. If a transaction's seller ID doesn't match the authorized seller ID for the given product ID (and the product ID exists in authorized_sellers), it's considered unauthorized and added to the unauthorized_sales list.
    for transaction in data['salesTransactions']:
        product_id = transaction['productID']
        seller_id = transaction['sellerID']
        if product_id in authorized_sellers and authorized_sellers[product_id] != seller_id:
            unauthorized_sales.append({'productID': product_id, 'unauthorizedSellerID': seller_id})

    # Response: Returns a JSON response with unauthorized sales transactions and a 200 OK status code if the request is processed successfully.
    return jsonify({'unauthorizedSales': unauthorized_sales}), 200

# Application Entry Point: The standard Python idiom for executing the application. When you run this script directly (not importing it in another script), it starts the Flask development server with debug mode enabled. Debug mode allows for automatic application reloading during development and provides a debugger if something goes wrong.
if __name__ == '__main__':
    app.run(debug=True)
