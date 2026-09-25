import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".taskcli.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def add_task(title):
    with get_conn() as conn:
        cur = conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        return cur.lastrowid

def list_tasks(show_done=False):
    with get_conn() as conn:
        query = "SELECT * FROM tasks"
        if not show_done:
            query += " WHERE done = 0"
        query += " ORDER BY id DESC"
        return conn.execute(query).fetchall()

def complete_task(task_id):
    with get_conn() as conn:
        cur = conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        return cur.rowcount

def delete_task(task_id):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        return cur.rowcount
