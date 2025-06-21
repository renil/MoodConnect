from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# --- Routes ---

# 1. The main dashboard route
@app.route('/')
def dashboard():
    """Renders the main dashboard page."""
    # This function simply serves the index.html file from the 'templates' folder.
    return render_template('index.html')

# 2. The API route to simulate a stress alert
@app.route('/trigger_alert')
def trigger_alert():
    """
    This is our "Wizard of Oz" endpoint.
    When called, it simulates the AI detecting a high-stress event.
    """
    # In a real app, this data would come from a complex model. Here, we just hardcode it.
    alert_data = {
        'status': 'alert',
        'heart_rate': '125 bpm',
        'stress_level': 'High',
        'alert_message': "ALERT: High stress pattern detected. Possible sensory overload."
    }
    # Return the data as a JSON response, which our webpage can easily use.
    return jsonify(alert_data)


# --- Run the App ---

if __name__ == '__main__':
    # The debug=True flag allows for live reloading when you save changes.
    app.run(debug=True)