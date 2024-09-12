import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create SQLite connection
def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message TEXT)')
    conn.commit()
    conn.close()

@app.route('/api/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message')

    # Insert the message into the SQLite database
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (message) VALUES (?)', (message,))
    conn.commit()
    conn.close()

    return jsonify({'response': f'Received and stored: {message}'})

@app.route('/api/messages', methods=['GET'])
def get_messages():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    conn.close()
    return jsonify(messages)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)

