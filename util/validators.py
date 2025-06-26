from util.exceptions import ValidationError

def validate_name(name):
    """
    Validates that the name is a non-empty string.

    Parameters:
        name (str): The name to validate.

    Raises:
        ValidationError: If name is not a non-empty string.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValidationError("Name must be a non-empty string.", field="name", value=name)


def validate_task_id(task_id):
    """
    Validates that the task ID is a positive integer.

    Parameters:
        task_id (int)

    Raises:
        ValidationError: If task_id is not a positive integer.
    """
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValidationError("Task ID must be a positive integer.", field="Task ID", value=task_id)
    

def validate_user_id(user_id):
    """
    Validates that the user ID is a positive integer.

    Parameters:
        user_id (int)

    Raises:
        ValidationError: If user_id is not a positive integer.
    """
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValidationError("User ID must be a positive integer.", field="User ID", value=user_id)  


def validate_string(string, field="input"):
    """
    Validates that the provided string is non-empty.

    Parameters:
        string (str)
        field (str)

    Raises:
        ValidationError: If the string is empty or not a string type.
    """
    if not isinstance(string, str) or not string.strip():
        raise ValidationError(f"{field} must be a non-empty string.", field=field, value=string)


def validate_status(status):
    """
    Validates that the task status is one of the allowed values.

    Parameters:
        status (str)

    Raises:
        ValidationError: If status is not 'to do', 'in progress', or 'done'.
    """
    valid_statuses = ("to do", "in progress", "done")
    if status.lower() not in valid_statuses:
        raise ValidationError("Please enter a valid status (To Do, In Progress, Done).", field="status", value=status)


def validate_priority(priority):
    """
    Validates that the task priority is one of the allowed values.

    Parameters:
        priority (str)

    Raises:
        ValidationError: If priority is not 'low', 'medium', or 'high'.
    """
    valid_priorities = ("low", "medium", "high")
    if priority.lower() not in valid_priorities:
        raise ValidationError("Please enter a valid priority (Low, Medium, High).", field="priority", value=priority)


