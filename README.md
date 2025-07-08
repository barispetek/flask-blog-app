# 📝 Flask Blog App

A clean and functional multi-user blog platform built with Flask.  
Users can register, log in, and manage their personal posts through a minimal, Bootstrap-styled interface.

---

## 🚀 Features

- 🔐 **Authentication:** Register, login, logout with secure password hashing  
- 🧾 **CRUD for Blog Posts:** Create, edit, delete posts tied to user accounts  
- 💡 **Flash Messages:** User-friendly feedback throughout the app  
- 🎨 **Responsive UI:** Clean design with Bootstrap 5 and custom CSS  
- 🧱 **Jinja2 Templates:** DRY structure using a `base.html` layout  
- 🔍 **Search Functionality:** Search posts by title within user’s dashboard  
- 📡 **RESTful API (V3):** JSON-based API with authentication

---

## 🛠️ Tech Stack

- Python 3.x  
- Flask  
- SQLite (for development)  
- Flask-Login  
- Bootstrap 5  
- Jinja2

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/barispetek/flask-blog-app.git
cd flask-blog-app

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Run the app
python app.py
