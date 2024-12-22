from flask import Flask, render_template, jsonify, request
from datetime import datetime
from db import db, Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.serialize() for todo in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    new_todo = Todo(
        name=data['name'],
        due_date=datetime.strptime(data['due_date'], '%Y-%m-%d').date(),
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.serialize()), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Todo deleted"})
    return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
