from flask import Blueprint, request
from services.taskManager import TaskManager

user_bp = Blueprint('user_routes', __name__)
tm = TaskManager()                

# --- CREATE ---
@user_bp.route('/', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        tm.create_user(data["user_id"], data["name"], data["email"])
        return {"message": "User created"}, 201
    except Exception as e:
        return {"error": str(e)}, 400   
     

# --- READ ALL ---
@user_bp.route('/', methods=['GET'])
def list_users():
    try:
        return [u.to_dict() for u in tm.get_all_users()], 200
    except Exception as e:
        return {"error": str(e)}, 500
    

# --- READ ONE ---
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = tm.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user.to_dict(), 200
    except Exception as e:
        return {"error": str(e)}, 400
    
    
# --- DELETE ---
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        tm.delete_user(user_id)
        return {"message": "User deleted"}, 200
    except Exception as e:
        return {"error": str(e)}, 400
    

# --- VIEW TASKS BY USER ---         
@user_bp.route('/<int:user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id):
    user = tm.get_user(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return [t.to_dict() for t in user.tasks], 200    
