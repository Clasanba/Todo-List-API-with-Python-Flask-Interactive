from flask import Flask,jsonify,request
import json 
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False },
    {"label": "My second task", "done": False }
    ]

@app.route('/todos', methods=['GET'])
def to_dos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    print("Incoming request with the following body", decoded_object)
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)








if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)