from db.connector import get_db_connection
from models.user import User
from models.tasks import Task
from util.exceptions import InvalidInputError

class TaskManager:

# --- Executes To Connect To The Required DB ---    
    def __init__(self):
        try:
            self.conn = get_db_connection()
        except InvalidInputError as e:
            raise    
        self.users = {}
        self.tasks = {}
        self._load_users_from_db()
        self._load_tasks_from_db() 


# --- Using Cursor, Loads All User Info From DB ---
    def _load_users_from_db(self):
        with self.conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM users")
            for row in cur.fetchall():
                user = User(row["user_id"], row["name"], row["email"])
                self.users[user.user_id] = user
                print("Loaded users at startup:", list(self.users.keys()))


# --- Using Cursor, Loads All Tasks' Info From DB ---
    def _load_tasks_from_db(self):
        with self.conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM tasks")
            for row in cur.fetchall():
                task = Task(
                    row["task_id"], row["title"], row["description"],
                    row["due_date"],
                    priority=Task._REVERSE_PRIORITY.get(row["priority"], "Medium"),
                    status=row["status"]
                )
                if row["user_id"] in self.users:         # Used To assign a task to a particular user_id
                    user = self.users[row["user_id"]]
                    task.assign_to(user)
                    user.add_task(task)
                self.tasks[task.task_id] = task

   
    # ----------- User Operations -----------
   
 # --- Creates A New User ---  
    def create_user(self, user_id, name, email):
        if user_id in self.users:                        # If user exists, raise an error
            raise ValueError("User ID already exists.")

        user = User(user_id, name, email)
        self.users[user_id] = user

        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO users (user_id, name, email) VALUES (%s, %s, %s)",
                        (user_id, name, email))
            self.conn.commit()


# --- Using Cursor, Returns All User Info From DB ---
    def get_all_users(self):
        return list(self.users.values())


# --- Using Cursor, Returns The Chosen User Info From DB ---
    def get_user(self, user_id):
        return self.users.get(user_id)


# --- Using Cursor, Deletes The Chosen User ---
    def delete_user(self, user_id):
        if user_id not in self.users:
            raise ValueError("User not found.")
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            self.conn.commit()
        del self.users[user_id]

   
    # ----------- Task Operations -----------
    
 # --- Creates A Task ---   
    def create_task(self, title, description, due_date, priority, user_id):
        user_id = int(user_id)                 
        if user_id not in self.users:
            raise ValueError("User not found.")


        default_status = "pending"
        priority_int = Task._PRIORITY_MAP.get(priority.lower(), 2)

        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO tasks 
                (title, description, status, priority, user_id, due_date)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    title,
                    description,
                    default_status,
                    priority_int,
                    user_id,
                    due_date
                )
            )
            self.conn.commit()
            task_id = cur.lastrowid  # fetch the new ID

    # This part is outside the 'with' block
            task = Task(task_id, title, description, due_date, priority, default_status)
            user = self.get_user(user_id)
            task.assign_to(user)
            user.add_task(task)
            self.tasks[task_id] = task


# --- Using Cursor, Returns All Task Info From DB ---
    def get_all_tasks(self):
        return list(self.tasks.values())


# --- Using Cursor, Returns The Chosen Task Info From DB ---
    def get_task(self, task_id):
        return self.tasks.get(task_id)


# --- Using Cursor, Updates Status Of The Chosen Task And Commits It To DB ---
    def update_task_status(self, task_id, new_status):
        task = self.get_task(task_id)
        if not task:
            raise ValueError("Task not found.")
        task.update_status(new_status)
        with self.conn.cursor() as cur:
            cur.execute("UPDATE tasks SET status = %s WHERE task_id = %s",
                        (task.status, task_id))
            self.conn.commit()


# --- Using Cursor, Updates Priority Of The Chosen Task And Commits It To DB ---
    def update_task_priority(self, task_id, new_priority):
        task = self.get_task(task_id)
        if not task:
            raise ValueError("Task not found.")
        task.update_priority(new_priority)
        with self.conn.cursor() as cur:
            cur.execute("UPDATE tasks SET priority = %s WHERE task_id = %s",
                        (task.priority_as_int(), task_id))
            self.conn.commit()


# --- Using Cursor, Deletes Task From DB ---
    def delete_task(self, task_id):
        if task_id not in self.tasks:
            raise ValueError("Task not found.")
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
            self.conn.commit()
        del self.tasks[task_id]


# --- Closes DB Connection ---
    def close(self):
        self.conn.close()

