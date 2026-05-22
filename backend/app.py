from flask import Flask, jsonify, request
from flask_cors import CORS
from database import Database

app = Flask(__name__)
CORS(app)
db = Database()

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(db.get_all())

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title', '').strip()
    if not title:
        return jsonify({'error': 'title required'}), 400
    task = db.add(title)
    return jsonify(task), 201

@app.route('/api/tasks/<int:task_id>/toggle', methods=['PUT'])
def toggle_task(task_id):
    task = db.toggle(task_id)
    if not task:
        return jsonify({'error': 'not found'}), 404
    return jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db.delete(task_id)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
