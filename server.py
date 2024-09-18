from flask import Flask, jsonify
from flask_socketio import SocketIO, send
from datetime import datetime
import json
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)
# In-memory message store
messages = []

# Load messages from file (for recoverability)
def load_messages():
    global messages
    try:
        with open('messages.json', 'r') as file:
            messages = json.load(file)
    except FileNotFoundError:
        messages = []

# Save messages to file (for recoverability)
def save_messages():
    with open('messages.json', 'w') as file:
        json.dump(messages, file)

# REST API to get the current message count
@app.route('/messages/count', methods=['GET'])
def message_count():
    return jsonify({"count": len(messages)})

# REST API to get all messages (for history)
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

# WebSocket event handler for receiving and broadcasting messages
@socketio.on('message')
def handle_message(message):
    msg = {
        'text': message,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    messages.append(msg)
    save_messages()  # Persist the message after every update
    send(msg, broadcast=True)  # Broadcast the message to all clients

# Error handler for recoverability in case of server errors
@app.errorhandler(500)
def internal_error(error):
    return "Server encountered an internal error.", 500

# Load messages at startup (recoverability)
load_messages()

# Run the Flask app with WebSocket support
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
