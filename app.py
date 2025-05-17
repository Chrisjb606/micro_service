### 1. app.py
```python
from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Database connection parameters from environment
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Simple health check
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

# Example GET endpoint
@app.route('/items', methods=['GET'])
def get_items():
    conn = psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM items;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    items = [{'id': r[0], 'name': r[1]} for r in rows]
    return jsonify(items)

# Example POST endpoint
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    name = data.get('name')
    conn = psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name) VALUES (%s) RETURNING id;", (name,))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': new_id, 'name': name}), 201

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
```