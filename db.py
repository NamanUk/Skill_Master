import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # your host
            user='root',  # your database user
            password='root',  # your database password
            database='skill_master'  # your database name
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None