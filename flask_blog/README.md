# Mini Flask Blog

A minimal, clean Flask blog with authentication and CRUD for posts.

## Features
- Register / Login / Logout (Flask-Login, Flask-WTF, hashed passwords)
- Create, edit, delete posts (only the author can edit/delete)
- SQLite database (SQLAlchemy)
- Bootstrap styling + small dark theme CSS
- CSRF protection

## Quickstart

```bash
# 1) Create and activate a virtual environment (Linux/macOS)
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run
python run.py
# App will be at http://127.0.0.1:5000
```

> First run will auto-create the SQLite database `blog.db`.

## Environment variables (optional)
- `SECRET_KEY` – set a strong random string in production
- `DATABASE_URL` – default is `sqlite:///blog.db`

## Project Structure
```
flask_blog/
  app/
    __init__.py
    models.py
    forms.py
    routes.py
    templates/
      base.html
      index.html
      login.html
      register.html
      create_post.html
      edit_post.html
    static/
      style.css
  run.py
  requirements.txt
  README.md
```
