import os

BASE_DIR = os.path.dirname(os.path.abspath(file))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "logs.db")

os.makedirs(DATA_DIR, exist_ok=True)
