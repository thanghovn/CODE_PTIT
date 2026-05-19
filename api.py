import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_FILE = 'tasks.json'



def load_data():
    if not os.path.exists(DATA_FILE):
        default_tasks = [
            {"id": 1, "title": "Học Flask", "description": "Tạo API quản lý công việc", "done": False},
            {"id": 2, "title": "Học Tkinter", "description": "Thiết kế giao diện cho ứng dụng", "done": True}
        ]
        save_data(default_tasks)
        return default_tasks

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


tasks = load_data()



# API 1: Lấy danh sách hoặc tìm kiếm theo tiêu đề
@app.route('/tasks', methods=['GET'])
def get_tasks():
    search_query = request.args.get('title', '').lower()
    if search_query:
        filtered_tasks = [t for t in tasks if search_query in t['title'].lower()]
        return jsonify(filtered_tasks), 200
    return jsonify(tasks), 200


# API 2: Lấy 1 công việc
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Không tìm thấy công việc"}), 404
    return jsonify(task), 200


# API 3: Thêm công việc
@app.route('/tasks', methods=['POST'])
def add_task():
    global tasks
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Thiếu thông tin bắt buộc"}), 400

    # Kiểm tra trùng lặp
    for t in tasks:
        if t['title'] == data['title'] and t['description'] == data['description']:
            return jsonify({"error": "Công việc này đã tồn tại!"}), 400

    new_id = tasks[-1]['id'] + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": data['title'],
        "description": data['description'],
        "done": data.get('done', False)
    }

    tasks.append(new_task)
    save_data(tasks)  # LƯU VÀO FILE

    return jsonify(new_task), 201


# API 4: Cập nhật công việc
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    global tasks
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Không tìm thấy công việc"}), 404

    data = request.get_json()

    # Kiểm tra trùng lặp với công việc khác (khác ID)
    check_title = data.get('title', task['title'])
    check_desc = data.get('description', task['description'])
    for t in tasks:
        if t['id'] != task_id and t['title'] == check_title and t['description'] == check_desc:
            return jsonify({"error": "Thông tin cập nhật bị trùng với một công việc khác!"}), 400

    if 'title' in data: task['title'] = data['title']
    if 'description' in data: task['description'] = data['description']
    if 'done' in data: task['done'] = data['done']

    save_data(tasks)  # LƯU VÀO FILE

    return jsonify(task), 200


# API 5: Xóa công việc
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Không tìm thấy công việc"}), 404

    tasks = [task for task in tasks if task["id"] != task_id]
    save_data(tasks)  # LƯU VÀO FILE

    return jsonify({"message": "Đã xóa công việc"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)