import unittest
import os
import json
from todo import TodoList


class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.filename = "test_todos.json"
        self.todo_list = TodoList(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_todo(self):
        self.todo_list.add_todo("Test task")
        self.assertEqual(len(self.todo_list.list_todos()), 1)
        self.assertEqual(self.todo_list.list_todos()[0]['task'], "Test task")

    def test_list_todos(self):
        self.assertEqual(self.todo_list.list_todos(), [])
        self.todo_list.add_todo("Test task")
        self.assertEqual(len(self.todo_list.list_todos()), 1)

    def test_save_and_load_from_file(self):
        self.todo_list.add_todo("Task 1")
        self.todo_list.add_todo("Task 2")

        new_todo_list = TodoList(self.filename)
        self.assertEqual(len(new_todo_list.list_todos()), 2)
        self.assertEqual(new_todo_list.list_todos()[0]['task'], "Task 1")
        self.assertEqual(new_todo_list.list_todos()[1]['task'], "Task 2")

    def test_load_from_nonexistent_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        new_todo_list = TodoList(self.filename)
        self.assertEqual(new_todo_list.list_todos(), [])

    def test_load_from_invalid_json_file(self):
        with open(self.filename, 'w') as f:
            f.write("invalid json")
        new_todo_list = TodoList(self.filename)
        self.assertEqual(new_todo_list.list_todos(), [])

    def test_autosave_on_add(self):
        self.todo_list.add_todo("Autosave test")
        with open(self.filename, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['task'], "Autosave test")


if __name__ == '__main__':
    unittest.main()
