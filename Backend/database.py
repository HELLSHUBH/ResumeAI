import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT", "3306")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    missing_vars = []

    if not host:
        missing_vars.append("DB_HOST")
    if not port:
        missing_vars.append("DB_PORT")
    if not user:
        missing_vars.append("DB_USER")
    if not password:
        missing_vars.append("DB_PASSWORD")
    if not database:
        missing_vars.append("DB_NAME")

    if missing_vars:
        print("Missing database environment variables:", missing_vars)
        return None

    try:
        connection = mysql.connector.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=database,
            connection_timeout=10
        )
        return connection

    except mysql.connector.Error as err:
        print("Database connection failed")
        print("Error number:", err.errno)
        print("SQL state:", err.sqlstate)
        print("Message:", err.msg)
        return None

    except Exception as error:
        print("Unexpected database error:", error)
        return None