import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        # database=os.getenv("DB_NAME")

    )

def execute_query(query, params=None, fetch=False):
    conn = connect_db()
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("Use HOSPITAL_DB")
    cursor.execute(query, params)
    if fetch:
        result = cursor.fetchall()
        conn.close()
        return result
    else:
        conn.commit()
        conn.close()
