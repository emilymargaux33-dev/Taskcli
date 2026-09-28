from flask import Flask, jsonify, request
import taskcli.db as db

app = Flask(__name__)
db.init_db()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    rows = db.list_tasks(all_tasks=True)
    data = []
    for r in rows:
        # r = (id, title, done, priority) ou selon ton db
        data.append({"id": r[0], "title": r[1], "done": bool(r[2]), "priority": r[3]})
    return jsonify(data)

@app.route("/tasks", methods=["POST"])
def create_task():
    j = request.get_json() or {}
    title = j.get("title") or request.args.get("title")
    priority = j.get("priority", "medium")
    if not title:
        return jsonify({"error": "title requis"}), 400
    db.add_task(title, priority)
    return jsonify({"status": "ok", "title": title})

@app.route("/")
def home():
    return jsonify({"message": "TaskAPI by Junior is running", "endpoints": ["/tasks"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
