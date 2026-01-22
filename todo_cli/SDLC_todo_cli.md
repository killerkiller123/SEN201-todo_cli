# SDLC for Project "todo_cli"

ProjectName: todo_cli  
Primary modules / nomenclature used in implementation:
- Package / module: `todo_cli`
- Entry point: `todo_cli/main.py`
- Storage module: `todo_cli/storage.py`
- Persistent data file: `storage.json`
- Data model: `ToDoItem`

1. Planning
- Goal: Build a simple CLI To-Do application to add/list/complete tasks and persist them to `storage.json`.
- Stakeholders: Student (developer), Instructor (evaluator).

2. Requirements
- Functional:
  - Add a task with title and optional description.
  - List tasks (id, title, status).
  - Mark task complete by id.
  - Persist tasks to `storage.json`.
- Non-functional:
  - CLI, standard-library only, human-readable JSON.

3. Design
- Components:
  - `todo_cli/main.py` — CLI and command dispatch.
  - `todo_cli/storage.py` — `load_todos()` and `save_todos(todos)`.
- Data model: ToDoItem JSON object with fields:
  - id: integer
  - title: string
  - description: string
  - completed: boolean

4. Implementation
- See `todo_cli` package files for implementation naming matching this document.

5. Testing
- Manual test steps:
  - Add tasks, list them, mark one complete, list again.
- Optional unit tests may be added later.

6. Deployment
- Push code to GitHub repository.

7. Maintenance
- Open issues for features like edit/delete or add priorities.

All names used here (project name, files, data model) match the implementation exactly.
