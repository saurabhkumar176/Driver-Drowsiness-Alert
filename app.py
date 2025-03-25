from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_detection():
    username = request.form['username']
    password = request.form['password']
    
    # You can add login validation here if needed.
    if username == "admin" and password == "password":  # Example credentials
        subprocess.Popen(["python", "drowsiness_detect.py"])  # Run your detection script
        return "Drowsiness detection started! Close this tab after viewing the console."
    else:
        return "Invalid credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
