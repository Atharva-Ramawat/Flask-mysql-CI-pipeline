import time
import mysql.connector
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    # RETRY LOGIC: The DB takes longer to start than the App.
    # We must wait for it, or the app will crash immediately.
    retries = 5
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host='mysql-db',      
                user='root',
                password='password',
                database='testdb'
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Database not ready yet... waiting. Error: {err}")
            retries -= 1
            time.sleep(5)
    return None

@app.route('/')
def hello():
    conn = get_db_connection()
    if conn is None:
        return "Error: Could not connect to the Database."
    
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, count INT)")
    
    # Insert a visit
    cursor.execute("INSERT INTO visits (count) VALUES (1)")
    conn.commit()
    
    # Count total visits
    cursor.execute("SELECT COUNT(*) FROM visits")
    count = cursor.fetchone()[0]
    
    conn.close()
    return f"Hello! I have been visited {count} times.\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)