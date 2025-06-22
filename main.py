from flask import Flask, render_template, jsonify
import random

# Initialize the Flask application
app = Flask(__name__)

# --- Simulated Biometric State ---
current_heart_rate = 85
current_stress_level = 'Calm'
alert_active = False  # Track if alert is currently active

HEART_RATE_ALERT_THRESHOLD = 120
STRESS_LEVELS = ['Calm', 'Mild', 'Elevated', 'High']

# --- Helper Functions ---
def get_dynamic_heart_rate():
    global current_heart_rate
    # Simulate heart rate with some random walk
    change = random.randint(-2, 4)
    current_heart_rate = max(60, min(140, current_heart_rate + change))
    return current_heart_rate

def get_dynamic_stress_level(hr):
    if hr < 90:
        return 'Calm'
    elif hr < 105:
        return 'Mild'
    elif hr < 120:
        return 'Elevated'
    else:
        return 'High'

# --- Routes ---

@app.route('/')
def dashboard():
    """Renders the main dashboard page."""
    # This function simply serves the index.html file from the 'templates' folder.
    return render_template('index.html')

@app.route('/biometrics')
def biometrics():
    """
    Endpoint to get the current simulated biometric data.
    This can be polled by the front end to get real-time updates.
    """
    hr = get_dynamic_heart_rate()
    stress = get_dynamic_stress_level(hr)
    return jsonify({
        'heart_rate': f'{hr} bpm',
        'stress_level': stress
    })

@app.route('/trigger_alert', methods=['GET', 'POST'])
def trigger_alert():
    global alert_active
    hr = get_dynamic_heart_rate()
    stress = get_dynamic_stress_level(hr)
    alert = hr >= HEART_RATE_ALERT_THRESHOLD or stress == 'High'
    # If alert is not active and threshold is crossed, trigger alert
    if alert and not alert_active:
        alert_active = True
        status = 'alert'
        message = "ALERT: High stress pattern detected. Possible sensory overload."
    elif not alert:
        alert_active = False
        status = 'ok'
        message = "All signals normal."
    else:
        status = 'no-repeat'  # Alert already active, don't repeat
        message = "Alert already shown."
    return jsonify({
        'status': status,
        'heart_rate': f'{hr} bpm',
        'stress_level': stress,
        'alert_message': message
    })

@app.route('/acknowledge_alert', methods=['POST'])
def acknowledge_alert():
    global alert_active
    alert_active = False
    return jsonify({'status': 'acknowledged'})

# --- Run the App ---

if __name__ == '__main__':
    # The debug=True flag allows for live reloading when you save changes.
    app.run(debug=True)