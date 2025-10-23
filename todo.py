"""Simple TODO list application."""
import json


class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.load_from_file(self.filename)

    def add_todo(self, task):
        """Add a new todo item."""
        self.todos.append({'task': task, 'completed': False})
        self.save_to_file(self.filename)

    def list_todos(self):
        """List all todos."""
        return self.todos

    def save_to_file(self, filename):
        """Save todos to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.todos, f, indent=4)

    def load_from_file(self, filename):
        """Load todos from a JSON file."""
        try:
            with open(filename, 'r') as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []
        except json.JSONDecodeError:
            self.todos = []


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_todo("Learn about Jules")
    print(todo_list.list_todos())
