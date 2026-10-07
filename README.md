# 🐍 Django Full-Stack Web Application & Polling Platform

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A robust, full-stack **Django** web application featuring secure user authentication, accounts management, dynamic database querying with Django ORM, and an interactive voting/polling system.

---

## ✨ Features
- **Accounts & Authentication**: User registration, login, logout, password resets, and session management.
- **Polls Engine**: Create questions, voting choices, real-time vote tallying, and results visualizer.
- **Django Admin**: Customized administrative interface for managing users, questions, and responses.
- **MVT Architecture**: Strict separation of Model, View, and Template logic.
- **CSRF & Security**: Built-in Django protections against CSRF, SQL Injection, and XSS.

---

## 📂 Project Structure
```
Django_app/
├── accounts/                   # User authentication & profile management
├── polls/                      # Voting & poll question application
├── django_app/                 # Project settings, routing & WSGI/ASGI
├── templates/                  # HTML templates with Django Template Language
├── manage.py                   # Django CLI management script
└── requirements.txt
```

---

## 🚀 Setup & Execution
```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations & run server
python manage.py migrate
python manage.py runserver
# Open http://127.0.0.1:8000/
```

---

## 👨‍💻 Author
**Deepak Raj** — [GitHub (@Deepak8081)](https://github.com/Deepak8081)
