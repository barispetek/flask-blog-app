# 📝 Flask Blog App
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-🐳-blue)](https://www.docker.com/)

A simple yet professional blog application built with Flask, PostgreSQL, and Docker.  
It includes user authentication, post creation/editing/deletion, and a clean Bootstrap-based UI.

---

## 🚀 Features

- User registration & login system (Flask-Login, hashed passwords)
- Post creation, editing, and deletion
- PostgreSQL database with SQLAlchemy ORM
- WTForms for form handling and validation
- Dockerized setup with separate services for `web` and `db`
- Environment variables via `.env`
- Clean and responsive Bootstrap 5 interface

---

## ⚙️ Technologies

- Python 3.11
- Flask
- Flask-WTF
- Flask-Login
- Flask-SQLAlchemy
- PostgreSQL
- Docker & Docker Compose
- HTML / Jinja2 / Bootstrap 5

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd flask-blog-app

#Set-up .env
SECRET_KEY=your-secret-key
DEBUG=True

POSTGRES_DB=flask_blog
POSTGRES_USER=yourusername
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=db
POSTGRES_PORT=5432

#Build & run with Docker
docker-compose up --build

#Create database tables
docker-compose exec web python create_table.py
