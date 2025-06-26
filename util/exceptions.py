class TaskManagerException(Exception):
    """
    Base exception class for all custom exceptions in the Task Manager application.
    """
    pass


class InvalidInputError(TaskManagerException):
    """
    Exception raised when user input is invalid or cannot be processed.

    Attributes:
        message (str): Explanation of the error.
        org_exception (Exception, optional): The original exception 
    """

    def __init__(self, message="Invalid input provided.", org_exception=None):
        """
        Initializes the InvalidInputError exception.

        Parameters:
            message (str): Error message 
            org_exception (Exception, optional): Original exception for debugging
        """
        super().__init__(message)
        self.org_exception = org_exception


class ValidationError(TaskManagerException):
    """
    Exception raised when a value fails validation rules.

    Attributes:
        message (str): Explanation of the validation error.
        field (str): The field that failed validation.
        value (Any): The invalid value that triggered the exception.
    """

    def __init__(self, message="Validation failed.", field=None, value=None):
        """
        Initializes the ValidationError exception.

        Parameters:
            message (str): error message
            field (str, optional): The name of the field that failed validation.
            value (Any, optional): The invalid value provided.
        """
        super().__init__(message)
        self.field = field
        self.value = value
