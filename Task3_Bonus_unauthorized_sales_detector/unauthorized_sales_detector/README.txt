Unauthorized Sales Detector API
This Flask application provides an API endpoint to detect unauthorized sales transactions based on provided datasets of product listings and actual sales records. It processes POST requests containing two lists: one with product listings (including product ID and authorized seller ID) and the other with actual sales transactions (including product ID and seller ID).

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Before you can run this application, you'll need to have Python and pip installed on your system. Python 3.6 or later is recommended. You can download Python from python.org.

First, clone this repository to your local machine

cd unauthorized_sales_detector

Set Up a Virtual Environment

Windows:
python3 -m venv venv
Activate the virtual environment:

MacOS :
source venv/bin/activate

On Windows:
.\venv\Scripts\activate

Install Dependencies
With the virtual environment activated, install the required Python packages:
pip install -r requirements.txt


Running the Application
With the dependencies installed, you can start the Flask application by running:
flask run
This command will start a development server on http://127.0.0.1:5000/.

Using the API
To use the API, send a POST request to http://127.0.0.1:5000/detect-unauthorized-sales with a JSON payload containing productListings and salesTransactions. For example:



{
  "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
  "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
}

You can use tools like Postman or curl to make requests to the API:

curl -X POST -H "Content-Type: application/json" -d '{"productListings": [{"productID": "123", "authorizedSellerID": "A1"}], "salesTransactions": [{"productID": "123", "sellerID": "B2"}]}' http://127.0.0.1:5000/detect-unauthorized-sales

Expected Response
The API will return a list of unauthorized sales transactions in the following format:

{
  "unauthorizedSales": [
    {"productID": "123", "unauthorizedSellerID": "B2"}
  ]
}
