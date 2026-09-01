import sqlite3
import os
from datetime import datetime
from sys_config import DB_PATH

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT,
                  email TEXT,
                  password TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_credentials(username, email, password):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO records (username, email, password, timestamp) VALUES (?,?,?,?)",
              (username, email, password, timestamp))
    conn.commit()
    conn.close()

def get_credentials(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT email, password FROM records WHERE username = ? ORDER BY id DESC LIMIT 1", (username,))
    row = c.fetchone()
    conn.close()
    return row