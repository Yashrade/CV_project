
from flask import Flask, render_template, jsonify
import threading
import subprocess
import os

app = Flask(__name__)
gesture_process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-gesture')
def start_gesture():
    global gesture_process
    if gesture_process is None:
        gesture_process = subprocess.Popen(['python', 'run_gesture.py'])
        return jsonify({'status': 'Gesture recognition started'})
    else:
        return jsonify({'status': 'Gesture recognition already running'})

@app.route('/stop-gesture')
def stop_gesture():
    global gesture_process
    if gesture_process is not None:
        gesture_process.terminate()
        gesture_process = None
        return jsonify({'status': 'Gesture recognition stopped'})
    else:
        return jsonify({'status': 'No gesture recognition running'})

if __name__ == '__main__':
    app.run(debug=True)
