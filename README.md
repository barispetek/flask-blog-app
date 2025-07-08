# 📝 Flask Blog App

A clean and functional multi-user blog platform built with Flask.  
Users can register, log in, and manage their personal blog posts via a simple and responsive UI.

---

## 🚀 Features

<<<<<<< HEAD
- 🔐 **User Authentication:** Register, login, logout with hashed passwords
- 📝 **Post Management:** Create, edit, delete, view, and search posts
- 🎨 **UI with Bootstrap 5:** Clean responsive design
- 🧠 **Form Validation:** With Flask-WTF
- ⚡ **Flash Messages:** Helpful feedback throughout the app
- 🧱 **Blueprint Structure:** Organized codebase
- 💾 **PostgreSQL Database:** Production-ready setup
=======
- 🔐 **Authentication:** Register, login, logout with secure password hashing  
- 🧾 **CRUD for Blog Posts:** Create, edit, delete posts tied to user accounts  
- 💡 **Flash Messages:** User-friendly feedback throughout the app  
- 🎨 **Responsive UI:** Clean design with Bootstrap 5 and custom CSS  
- 🧱 **Jinja2 Templates:** DRY structure using a `base.html` layout  
- 🔍 **Search Functionality:** Search posts by title within user’s dashboard  
- 📡 **RESTful API (V3):** JSON-based API with authentication
>>>>>>> origin/main

---

## 🛠️ Tech Stack

<<<<<<< HEAD
- Python 3.11+
- Flask
- Flask-Login
- Flask-WTF
- SQLAlchemy
- PostgreSQL
- Bootstrap 5
=======
- Python 3.x  
- Flask  
- SQLite (for development)  
- Flask-Login  
- Bootstrap 5  
- Jinja2
>>>>>>> origin/main

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/barispetek/flask-blog-app.git
cd flask-blog-app

# (Optional) Create virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Windows
# source .venv/bin/activate    # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure Environment
# Create a .env file in the root directory
SECRET_KEY=your-secret-key
DEBUG=True
POSTGRES_DB=flask_blog
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

#Initialize Database Tables
python create_table.py

# Run the app
python app.py

Then visit
👉 http://127.0.0.1:5000

