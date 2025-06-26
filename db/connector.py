import mysql.connector

# --- DB CONNECTION ---
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',            # All these information are to be changed based on database used
        password='Escanor@12345',        
        database='TaskManagerDB'
    )


"""
The following Code can be used to create and use a databse in python itself (Remove the '#')
"""

#import mysql.connector
#from mysql.connector import errorcode                                   
#from util.exceptions import InvalidInputError                           

"""
 ---------------------------------------------------------------------
 Internal helpers
 ---------------------------------------------------------------------
"""

#def _create_database(cursor, db_name):                                  
#    """Create DB if it doesn't already exist."""                         
#    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")          
#    cursor.execute(f"USE {db_name}")                                     

#def _create_tables(cursor):                                             
#    """Create 'users' and 'tasks' tables if they don't exist."""         
#    cursor.execute("""
#        CREATE TABLE IF NOT EXISTS users (
#            user_id INT PRIMARY KEY,
#            name    VARCHAR(50) NOT NULL,
#            email   VARCHAR(50) NOT NULL UNIQUE
#        )
#    """)
#    cursor.execute("""
#        CREATE TABLE IF NOT EXISTS tasks (
#            task_id     INT PRIMARY KEY,
#            title       VARCHAR(50),
#            description TEXT,
#            status      VARCHAR(50),
#            priority    INT CHECK (priority BETWEEN 1 AND 3),
#            due_date    DATE,
#            user_id     INT,
#            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
#        )
#    """)

"""
 ---------------------------------------------------------------------
 Public API
 ---------------------------------------------------------------------
"""

#def get_db_connection():
#   """
#    Connect to MySQL, auto-create DB & tables, and return the live
#    connection.  Raises InvalidInputError for any connection issues.
#    """
#    DB_NAME = "TaskManagerDB"                                           
#    try:
#        #  Connect without specifying a database first
#        conn = mysql.connector.connect(
#            host="localhost",
#            user="root",
#            password="Escanor@12345"
#        )
#        with conn.cursor() as cur:
#            _create_database(cur, DB_NAME)                              
#            _create_tables(cur)                                         
#            conn.commit()                                               

        # Switch the connection to use our DB going forward
#        conn.database = DB_NAME                                         
#        return conn

    # ---------------- error handling ----------------
#    except mysql.connector.Error as err:                                
#        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#            msg = "Invalid MySQL username or password."
#        elif err.errno == errorcode.ER_BAD_DB_ERROR:
#            msg = f"Database '{DB_NAME}' cannot be created."
#        else:
#            msg = f"Database connection error: {err}"
#        raise InvalidInputError(msg, org_exception=err) from err        
