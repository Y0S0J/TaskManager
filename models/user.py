class User:
    """
    Represents a user who can be assigned tasks.

    Attributes:
        user_id (int): Unique ID of the user.
        name (str): Full name of the user.
        email (str): Email address of the user.
        tasks (list): List of tasks assigned to the user.
    """

# --- Executes To Get New User Values ---
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.tasks = []

# --- Appends A New Task To The Chosen User---
    def add_task(self, task):
        self.tasks.append(task)

# --- Removes A Chosen Task From The User ---
    def remove_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

# --- Returns All User Values In Dict Format ---  
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }
