from flask import Blueprint, request
from services.taskManager import TaskManager

task_bp = Blueprint('task_routes', __name__)
tm = TaskManager()                  

# --- CREATE ---
@task_bp.route('/', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        tm.create_task(
            data["title"], data["description"],
            data["due_date"], data["priority"], data["user_id"]
            )    
        return {"message": "Task created"}, 201
    except Exception as e:
        return{"error": str(e)},400
    

# --- READ ALL ---
@task_bp.route('/', methods=['GET'])
def list_tasks():
    try:
        return [t.to_dict() for t in tm.get_all_tasks()], 200
    except Exception as e:
        return {"error": str(e)}, 500
    

# --- READ ONE ---
@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = tm.get_task(task_id)
        if not task:
            return {"error": "Task not found"}, 404
        return task.to_dict(), 200
    except Exception as e:
        return {"error": str(e)}, 400
    

# --- UPDATE STATUS ---
@task_bp.route('/<int:task_id>/status', methods=['PUT'])
def update_status(task_id):
    try:
        data = request.get_json()
        tm.update_task_status(task_id, data["status"])
        return {"message": "Status updated"}, 200
    except Exception as e:
        return {"error": str(e)}, 400
    

# --- UPDATE PRIORITY ---
@task_bp.route('/<int:task_id>/priority', methods=['PUT'])
def update_priority(task_id):
    try:
        data = request.get_json()
        tm.update_task_priority(task_id, data["priority"])
        return {"message": "Priority updated"}, 200
    except Exception as e:
        return {"error": str(e)}, 400
    

# --- DELETE ---
@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        tm.delete_task(task_id)
        return {"message": "Task deleted"}, 200
    except Exception as e:
        return {"error": str(e)}, 400