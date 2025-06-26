class Task:
    """
    Represents a task with ID, title, description, due date, priority, and status.

    Attributes:
        task_id (int)
        title (str)
        description (str)
        due_date (str)
        priority (str)
        status (str)
        assigned_to (User)
    """

# --- Mapping For Cleaner Access For User And DB ---
    _PRIORITY_MAP = {"low": 1, "medium": 2, "high": 3}
    _REVERSE_PRIORITY = {1: "Low", 2: "Medium", 3: "High"}

# ---  Executes To Get All Information Required For A New Task ---
    def __init__(self, task_id, title, description, due_date,
                 priority="medium", status="pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority.lower()
        self.status = status.lower()
        self.assigned_to = None

# --- Assigns A Task To The Required User_ID ---
    def assign_to(self, user):
        self.assigned_to = user

# --- Updates The New Status Of A Chosen Task ---
    def update_status(self, new_status):
        self.status = new_status.lower()

# --- Update The New Priority Of A Chosen Task ---
    def update_priority(self, new_priority):
        self.priority = new_priority.lower()

# --- Priority Mapping ---
    def priority_as_int(self):
        return self._PRIORITY_MAP.get(self.priority, 2)

# --- Returns All Task Values In Dict Format---
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority.title(),
            "status": self.status.title(),
            "user_id": self.assigned_to.user_id if self.assigned_to else None
        }
