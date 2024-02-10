Optimal Interview Scheduler API
This Flask application provides an API endpoint to calculate the maximum number of non-overlapping job interviews one can attend based on provided start and end times.

Getting Started
These instructions will guide you on how to run and use the application on your local machine.

Prerequisites
Python 3.6 or higher
pip (Python package installer)
Installation
Clone the Repository

Use Git to clone the repository to your local machine
Set Up a Virtual Environment


python3 -m venv venv
source venv/bin/activate

Install Flask within your virtual environment:
pip install Flask
Running the Application
Start the Flask Server

Run the following command in the terminal to start the Flask development server:
flask run
The application will be accessible at http://127.0.0.1:5000/.

Using the API
To use the API, send a POST request to http://127.0.0.1:5000/schedule-interviews with a JSON payload containing start_times and end_times. For example:


{
  "start_times": [10, 20, 30, 40, 50, 60],
  "end_times": [15, 25, 35, 45, 55, 65]
}

You can use tools like curl or Postman to make the request:

Using curl:

curl -X POST -H "Content-Type: application/json" -d '{"start_times": [10, 20, 30, 40, 50, 60], "end_times": [15, 25, 35, 45, 55, 65]}' http://127.0.0.1:5000/schedule-interviews

Using Postman:
Set the request type to POST.
Enter the URL http://127.0.0.1:5000/schedule-interviews.
In the Headers section, set Content-Type to application/json.
In the Body section, choose raw and paste the JSON data.
Click Send.
