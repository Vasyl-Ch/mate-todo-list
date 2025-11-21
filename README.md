Mate Todo List
A Django-powered task manager for staying organized
This repository appears to be a Django-based todo list application, likely built for personal productivity or as a learning project. It features task creation, tagging, deadlines, and completion tracking, all wrapped in a clean, responsive interface. Whether you're managing daily chores or building a habit tracker, this app makes staying on top of your to-dos effortless and visually satisfying—turning chaos into clarity with just a few clicks.
Installing / Getting started
The fastest way to run the project locally:

git clone https://github.com/Vasyl-Ch/mate-todo-list.git
cd mate-todo-list
python -m venv venv
source venv/bin/activate          # Linux / macOS
# или: venv\Scripts\activate     # Windows
pip install django
python manage.py migrate
python manage.py runserver

Open http://127.0.0.1:8000 — your todo app is ready!

This starts the development server with a fresh SQLite database. All tasks and tags are stored locally.
Initial Configuration
No external services or keys required — everything works out of the box.
Developing
To start developing or extending the project:

git clone https://github.com/Vasyl-Ch/mate-todo-list.git
cd mate-todo-list
python -m venv venv
source venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver

All functionality lives in the single tasks app. Views are class-based (CBV), forms use ModelForm, and templates inherit from base.html.
Building
No separate build step is needed — just restart the server after code changes.
Features

Create, edit, delete tasks
One-click toggle complete / undo
Optional deadlines with visual “Overdue” badge
Create and manage tags
Assign multiple tags to tasks
Tasks automatically ordered (active first, newest on top)
Fully responsive Bootstrap 5 design
Clean, modern UI with hover effects
Basic tests included

Configuration
Only standard Django settings are used.
For production you may want to change in settings.py:

PythonDEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

No environment variables required.
Contributing
Contributions are very welcome!
Fork the repository, create a feature branch, commit your changes and open a Pull Request.
Quick workflow:

git checkout -b feature/your-feature
# make changes
git commit -m "Add your feature"
git push origin feature/your-feature
Please follow PEP 8 and add tests when possible.

Links

Repository: https://github.com/Vasyl-Ch/mate-todo-list

Licensing
The code in this project is licensed under the MIT license.
You are free to use, modify, and redistribute it for any purpose — personal or commercial.
