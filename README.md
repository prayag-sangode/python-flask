# 🚀 Flask CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built with **Flask**, **SQLAlchemy**, and **SQLite**.

This project demonstrates:

- Flask API development
- SQLite database integration
- SQLAlchemy ORM
- RESTful endpoints
- CRUD operations
- Python virtual environments

---

# Project Structure

```text
python-flask/
├── app.py
├── requirements.txt
├── README.md
└── instance/
    └── users.db
```

---

# Prerequisites

Install Python virtual environment support:

```bash
sudo apt update
sudo apt install python3.12-venv
```

Verify Python:

```bash
python3 --version
```

---

# Clone Repository

```bash
git clone <your-repository-url>
cd python-flask
```

Example:

```bash
git clone https://github.com/<username>/python-flask.git
cd python-flask
```

---

# Create Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Your prompt should look similar to:

```bash
(venv) ubuntu@devops-vm:~/python-flask$
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

Installed packages include:

- Flask
- Flask-SQLAlchemy
- SQLAlchemy

Verify installation:

```bash
pip list
```

---

# Run Application

Start the API server:

```bash
python app.py
```

Expected output:

```text
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://<SERVER_IP>:5000
```

---

# Verify Application

## Home Endpoint

```bash
curl http://localhost:5000
```

Response:

```json
{
  "message": "Flask CRUD API is running",
  "version": "1.0",
  "endpoints": [
    "/users",
    "/users/<id>"
  ]
}
```

---

# API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | / | Application Info |
| POST | /users | Create User |
| GET | /users | Get All Users |
| GET | /users/<id> | Get User By ID |
| PUT | /users/<id> | Update User |
| DELETE | /users/<id> | Delete User |

---

# Complete CRUD Example

## 1. Create User

```bash
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{
  "name":"Prayag",
  "email":"prayag@gmail.com"
}'
```

Response:

```json
{
  "message": "User created",
  "user": {
    "id": 1,
    "name": "Prayag",
    "email": "prayag@gmail.com"
  }
}
```

---

## 2. Create Another User

```bash
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{
  "name":"John",
  "email":"john@gmail.com"
}'
```

---

## 3. Get All Users

```bash
curl http://localhost:5000/users
```

Response:

```json
[
  {
    "id": 1,
    "name": "Prayag",
    "email": "prayag@gmail.com"
  },
  {
    "id": 2,
    "name": "John",
    "email": "john@gmail.com"
  }
]
```

---

## 4. Get User By ID

```bash
curl http://localhost:5000/users/1
```

Response:

```json
{
  "id": 1,
  "name": "Prayag",
  "email": "prayag@gmail.com"
}
```

---

## 5. Update User

```bash
curl -X PUT http://localhost:5000/users/1 \
-H "Content-Type: application/json" \
-d '{
  "name":"Prayag Sangode"
}'
```

Response:

```json
{
  "message": "User updated",
  "user": {
    "id": 1,
    "name": "Prayag Sangode",
    "email": "prayag@gmail.com"
  }
}
```

---

## 6. Verify Update

```bash
curl http://localhost:5000/users/1
```

Response:

```json
{
  "id": 1,
  "name": "Prayag Sangode",
  "email": "prayag@gmail.com"
}
```

---

## 7. Delete User

```bash
curl -X DELETE http://localhost:5000/users/2
```

Response:

```json
{
  "message": "User deleted"
}
```

---

## 8. Verify Delete

```bash
curl http://localhost:5000/users
```

Response:

```json
[
  {
    "id": 1,
    "name": "Prayag Sangode",
    "email": "prayag@gmail.com"
  }
]
```

---

# SQLite Database

The database is created automatically on first startup.

Location:

```text
instance/users.db
```

No manual database setup is required.

---

# Useful Commands

## Save Installed Packages

```bash
pip freeze > requirements.txt
```

## Deactivate Virtual Environment

```bash
deactivate
```

## Recreate Environment

```bash
rm -rf venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

# Troubleshooting

### Port Already In Use

Check which process is listening on port 5000:

```bash
sudo ss -lntp | grep 5000
```

Kill the process if necessary:

```bash
sudo kill -9 <PID>
```

---

### Module Not Found

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

---

### Check Database File

```bash
ls -l instance/
```

Expected:

```text
users.db
```

---

# Next Steps

After mastering this example, try extending it with:

- PostgreSQL
- Docker
- GitLab CI/CD
- Kubernetes
- Ingress
- JWT Authentication
- Swagger/OpenAPI Documentation

