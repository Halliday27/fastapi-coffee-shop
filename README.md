# FastAPI Expense Tracker API

A learning-focused FastAPI backend for user auth, categories, and expense tracking.

## Features
- JWT authentication (register/login)
- Password hashing with passlib/bcrypt
- Category management per user
- Expense CRUD per user
- Ownership checks for categories and expenses
- SQLite + SQLAlchemy ORM
- Interactive docs at `/docs`

## Run locally
```bash
pip install -r requirements.txt
python run.py
```

Then open:
- API docs: http://127.0.0.1:8000/docs

## Project structure
```text
app/
  config.py
  database.py
  dependencies.py
  main.py
  models/
  routers/
  schemas/
  utils/
requirements.txt
run.py
```
