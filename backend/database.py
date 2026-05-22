import json
import os

class Database:
    def __init__(self):
        self.file = 'tasks.json'
        if not os.path.exists(self.file):
            self._save([])

    def _load(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save(self, tasks):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)

    def get_all(self):
        return self._load()

    def add(self, title):
        tasks = self._load()
        task = {
            'id': len(tasks) + 1,
            'title': title,
            'done': False
        }
        tasks.append(task)
        self._save(tasks)
        return task

    def toggle(self, task_id):
        tasks = self._load()
        for task in tasks:
            if task['id'] == task_id:
                task['done'] = not task['done']
                self._save(tasks)
                return task
        return None

    def delete(self, task_id):
        tasks = self._load()
        tasks = [t for t in tasks if t['id'] != task_id]
        self._save(tasks)
