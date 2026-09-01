import sqlite3
from sys_config import DB_PATH

def get_credentials(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT verification_code, new_password FROM verification_logs WHERE username = ? ORDER BY id DESC LIMIT 1", (username,))
    row = c.fetchone()
    conn.close()
    return row  # (code, password) or None
