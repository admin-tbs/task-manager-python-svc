from flask import Flask, request
from storage import save_task, get_tasks, update_tasks, remove_task
from logger import log

app = Flask("user")
# app.logger()

@app.route("/tasks", methods=["POST"], endpoint='create_task')
@log
def create_task():
    data = request.json
    status = save_task(data)
    if status ==  True:
        return "Task Created Successfully", 200
    else:
        return "Failed while creating Task", 500

@app.route("/tasks", methods=["GET"])
@log
def read_tasks():
    return get_tasks(), 200

@app.route("/update/tasks", methods=["PUT"], endpoint = "edit_tasks")
@log
def update_task():
    data = request.json
    status, data = update_tasks(data)
    if status:
        return data, 200

@app.route("/tasks/<task_id>", methods=["DELETE"], endpoint = "del_task")
@log
def delete_task(task_id):
    status = remove_task(int(task_id))
    if status:
        return f"Deleted task -- {task_id}", 200
    else:
        return f"Failed to delete task -- {task_id}", 500

if __name__ == "__main__":
    app.run()