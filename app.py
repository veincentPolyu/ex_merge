from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
items = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(items), 200

@app.route('/todos', methods=['POST'])
def add_item():
    item = request.json

    # add item only if it is not already present
    if item in items:
        return jsonify({'error': 'Item already exists'}), 400
    else:
        items.append(item)
        return jsonify(item), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id >= len(items) or todo_id < 0:
        return jsonify({'error': 'Todo not found'}), 404
    todo = request.json
    items[todo_id] = todo
    return jsonify(todo), 200

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id >= len(items) or todo_id < 0:
        return jsonify({'error': 'Todo not found'}), 404
    todo = items.pop(todo_id)
    return jsonify(todo), 200

if __name__ == '__main__':
    app.run(debug=True)