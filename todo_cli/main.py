# todo_cli/main.py
# Entry point for the todo_cli app
import argparse
from todo_cli.storage import load_todos, save_todos

def add_task(title, description=""):
    todos = load_todos()
    next_id = max([t["id"] for t in todos], default=0) + 1
    todo = {"id": next_id, "title": title, "description": description, "completed": False}
    todos.append(todo)
    save_todos(todos)
    print(f"Added task {next_id}: {title}")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
        return
    for t in todos:
        status = "✓" if t.get("completed") else " "
        print(f"[{status}] {t['id']}: {t['title']} - {t.get('description','')}")

def complete_task(task_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == task_id:
            t["completed"] = True
            save_todos(todos)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task with id {task_id} not found.")

def main():
    parser = argparse.ArgumentParser(prog="todo_cli", description="Simple ToDo CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task title")
    p_add.add_argument("-d", "--description", default="", help="Task description")

    p_list = sub.add_parser("list", help="List tasks")

    p_complete = sub.add_parser("complete", help="Mark task as complete")
    p_complete.add_argument("id", type=int, help="Task id")

    args = parser.parse_args()
    if args.command == "add":
        add_task(args.title, args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.id)

if __name__ == "__main__":
    main()
