# 🚀 Mate Todo List

*A Django-powered task manager for staying organized*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains a Django-based todo list application, built for personal productivity and as a learning project. It features task creation, tagging, deadlines, and completion tracking, all wrapped in a clean, responsive interface. Whether you're managing daily chores or building a habit tracker, this app makes staying on top of your to-dos effortless and visually satisfying—turning chaos into clarity with just a few clicks.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vasyl-Ch/mate-todo-list.git
   cd mate-todo-list
   ```

2. **Set up a virtual environment**
   ```bash
   # Linux/macOS
   python -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser**
   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to see your todo app in action!

## 🛠 Features

- ✅ **Task Management**
  - Create, edit, and delete tasks
  - One-click toggle complete/undo
  - Optional deadlines with visual "Overdue" badge
  
- 🏷 **Tags & Organization**
  - Create and manage tags
  - Assign multiple tags to tasks
  - Tasks automatically ordered (active first, newest on top)
  
- 🎨 **UI/UX**
  - Fully responsive Bootstrap 5 design
  - Clean, modern interface with hover effects
  - Intuitive navigation

- 🧪 **Testing**
  - Basic test coverage included
  - Follows Django's testing framework

## ⚙️ Configuration

For production, you should update the following settings in `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'your-secret-key-here'
```

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

### Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Include docstrings for functions and classes
- Write tests for new features
- Keep commits atomic and well-documented

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Repository**: [github.com/Vasyl-Ch/mate-todo-list](https://github.com/Vasyl-Ch/mate-todo-list)
- **Issue Tracker**: [github.com/Vasyl-Ch/mate-todo-list/issues](https://github.com/Vasyl-Ch/mate-todo-list/issues)

---

