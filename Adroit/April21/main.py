
from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# Sample user for login
USER = {"username": "admin", "password": "admin123"}

# In-memory store for todos
todos = {
    1: {"task": "Learn REST", "done": True},
    2: {"task": "Build CRUD API", "done": True}
}

# JWT auth decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token.split(" ")[-1], app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401
        return f(*args, **kwargs)
    return decorated

# Login route
@app.route("/login", methods=["POST"])
def login():
    auth = request.json
    if auth["username"] == USER["username"] and auth["password"] == USER["password"]:
        token = jwt.encode({
            "user": auth["username"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config["SECRET_KEY"])
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401

# CRUD Routes (all protected)

@app.route("/todos", methods=["GET"])
@token_required
def get_todos():
    return jsonify(todos)

@app.route("/todos/<int:todo_id>", methods=["GET"])
@token_required
def get_todo(todo_id):
    return jsonify(todos.get(todo_id, {"error": "Not found"}))

@app.route("/todos", methods=["POST"])
@token_required
def create_todo():
    data = request.json
    todo_id = max(todos.keys(), default=0) + 1
    todos[todo_id] = {"task": data["task"], "done": False}
    return jsonify({"id": todo_id, "todo": todos[todo_id]}), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
@token_required
def update_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "Not found"}), 404
    todos[todo_id].update(request.json)
    return jsonify(todos[todo_id])

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
@token_required
def delete_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "Not found"}), 404
    del todos[todo_id]
    return jsonify({"message": "Deleted"}), 204

if __name__ == "__main__":
    app.run(debug=True)
