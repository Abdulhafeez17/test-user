import os
import subprocess
from flask import Flask
from datetime import datetime
import pytz
from waitress import serve  # Production-ready server for Windows

app = Flask(__name__)

# Your full name
NAME = "Abdul Hafeez"

@app.route('/htop')
def htop():
    # Get system username
    username = os.getlogin()
    
    # Get server time in IST
    ist_timezone = pytz.timezone('Asia/Kolkata')
    server_time_ist = datetime.now(ist_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Run the 'top' command and capture the output
    try:
        top_output = subprocess.check_output(['tasklist'], universal_newlines=True)
    except subprocess.CalledProcessError as e:
        top_output = f"Error occurred while running 'tasklist': {str(e)}"

    # Format the data to display on the webpage
    html_content = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {NAME}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time_ist}</p>
        <h2>Tasklist Command Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html_content


if __name__ == '__main__':
    # Use Waitress to serve the app in a production-ready manner
    serve(app, host='0.0.0.0', port=5000)
