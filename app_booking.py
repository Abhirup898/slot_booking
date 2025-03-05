from flask import Flask, request, jsonify
import random
import datetime

app = Flask(__name__)

# A simple route to handle slot booking
@app.route('/book-slot', methods=['POST'])
def book_slot():
    try:
        # Get the input data from the request
        patient_name = request.json.get('patient_name')
        date_str = request.json.get('date')  # e.g., "2025-03-09"
        time_str = request.json.get('time')  # e.g., "10:00:00+05:30"
        
        # Validate the input data
        if not patient_name or not date_str or not time_str:
            return jsonify({"error": "Patient name, date, and time are required"}), 400
        
        # Combine date and time into a single datetime object
        try:
            # Assuming the time string is in the ISO format (with timezone)
            datetime_str = f"{date_str}T{time_str}"
            date_time = datetime.datetime.fromisoformat(datetime_str)
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Expected valid ISO format."}), 400
        
        # Generate a unique booking number (you can customize this part)
        booking_number = f"#{random.randint(1000, 9999)}#"

        # Return the booking confirmation
        response = {
            "patient_name": patient_name,
            "booking_number": booking_number,
            "date": date_time.date().isoformat(),  # Return date separately
            "time": date_time.time().isoformat()  # Return time separately
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
   
