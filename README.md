# 📝 Flask Blog App

A simple yet functional blog application built with Flask.

Users can register, log in, and manage their own posts — including creating, editing, and deleting blog entries.  
This project is the first version (v1) of a series of progressively more advanced blog applications.

---

## 🚀 Features

- User authentication (register, login, logout)
- Create, read, update, and delete blog posts
- Posts tied to specific user accounts
- Flash message feedback system
- Responsive UI using Bootstrap
- Custom CSS styling
- Clean Flask file structure

---

## 🛠️ Tech Stack

- Python
- Flask
- SQLite
- Flask-Login
- Jinja2 Templates
- Bootstrap 5

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/barispetek/flask-blog-app.git
cd flask-blog-app

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Run the app
python app.py
