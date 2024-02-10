# Import necessary modules from Flask
from flask import Flask, request, jsonify

# Initialize a Flask application
app = Flask(__name__)

# Define a route that listens for POST requests on '/schedule-interviews'
@app.route('/schedule-interviews', methods=['POST'])
def schedule_interviews():
    # Get JSON data from the request
    data = request.get_json()

    # Validate the input data structure
    if not data or 'start_times' not in data or 'end_times' not in data:
        # Return an error response if validation fails
        return jsonify({'error': 'Invalid data format'}), 400

    # Calculate the maximum number of non-overlapping interviews
    max_interviews = calculate_max_interviews(data['start_times'], data['end_times'])

    # Return the result as a JSON response
    return jsonify({'max_interviews': max_interviews})

# Helper function to calculate the maximum number of non-overlapping interviews
def calculate_max_interviews(start_times, end_times):
    # Zip start and end times together and sort by end times
    intervals = sorted(zip(start_times, end_times), key=lambda x: x[1])
    count = 0  # Initialize counter for maximum interviews
    current_end_time = 0  # Track the end time of the last attended interview

    # Iterate through each interval
    for start, end in intervals:
        # If the start time is equal to or later than the current end time, attend the interview
        if start >= current_end_time:
            count += 1  # Increment the counter
            current_end_time = end  # Update the current end time

    # Return the total count of attended interviews
    return count

# Check if the script is executed directly (not imported)
if __name__ == '__main__':
    # Run the Flask application with debug mode enabled
    app.run(debug=True)

