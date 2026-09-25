import sqlite3, os
DB_PATH = os.path.expanduser("~/.taskcli.db")
def get_conn():
    return sqlite3.connect(DB_PATH)
def init_db():
    conn = get_conn()
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER DEFAULT 0, priority TEXT DEFAULT 'medium')")
    conn.commit()
    conn.close()
def add_task(title, priority="medium"):
    conn = get_conn()
    conn.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", (title, priority))
    conn.commit()
    conn.close()
def list_tasks(show_all=False):
    conn = get_conn()
    cur = conn.cursor()
    q = "SELECT id, title, done, priority FROM tasks" if show_all else "SELECT id, title, done, priority FROM tasks WHERE done=0"
    cur.execute(q)
    rows = cur.fetchall()
    conn.close()
    return rows
