from flask import Flask, request, jsonify
from Controller.ConnectionDBController import ConnectionDBController

from Model.TaskModel import TaskModel
from flask_cors import CORS #added to top of file


app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/*": {"origins": "*"}})

conn = ConnectionDBController.get_connection()
conn.row_factory = ConnectionDBController.dict_factory

@app.route('/')
def check():
    return 'OK'

@app.route('/api')
def check_api():
    return 'API is running'

@app.route('/api/tasks', methods=['GET'])
def api_get_tasks():
    return jsonify(TaskModel().get_tasks(conn))

@app.route('/api/tasks/<task_id>', methods=['GET'])
def api_get_task(task_id):
    return jsonify(TaskModel().get_task_by_id(conn, task_id))

@app.route('/api/tasks/add',  methods = ['POST'])
def api_add_task():
    task = request.get_json()
    return jsonify(TaskModel().insert_task(conn, task))

@app.route('/api/tasks/update',  methods = ['PUT'])
def api_update_task():
    task = request.get_json()
    return jsonify(TaskModel().update_task(conn, task))

@app.route('/api/tasks/delete/<task_id>',  methods = ['DELETE'])
def api_delete_task(task_id):
    return jsonify(TaskModel().delete_task(conn, task_id))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app