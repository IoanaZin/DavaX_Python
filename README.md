# 🔢 Math Microservice API – FastAPI + SQLite

## 🧠 Overview

This project is a lightweight **RESTful microservice** built with **FastAPI**, providing three core mathematical operations:

- `power`: computes `x^y`
- `factorial`: computes `n!`
- `fibonacci`: computes the n-th Fibonacci number

Each operation is exposed via a dedicated **POST endpoint**, with corresponding **GET endpoints** for viewing the operation history.  
Results are saved to a **SQLite database**, and all activity is logged to a `.log` file.

> 🔐 **Authentication required**: You must include the header `x-api-key: math123secret` in every request.

---

## 📦 Project Structure

math_api/
├── main.py # FastAPI app and routes
├── services.py # MathService (power, factorial, fibonacci)
├── db.py # SQLiteDatabase for persistence
├── logger.py # LoggerService for file-based logging
├── models.py # Pydantic request/response models
├── math_ops.db # SQLite database (auto-created)
├── math_api.log # Log file (auto-created)
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

## 🚀 How to Run Locally

### 1. Clone and set up environment

```bash
git clone https://github.com/IoanaZin/DavaX_Python_homework.git
cd DavaX_Python_homework
python -m venv .venv
.venv\Scripts\activate      # For Windows
pip install -r requirements.txt


---

## 🚀 How to Run Locally

### 1. Clone and set up environment

```bash
git clone https://github.com/IoanaZin/DavaX_Python_homework.git
cd DavaX_Python_homework
python -m venv .venv
.venv\Scripts\activate      # For Windows
pip install -r requirements.txt

### 2. Start the FastAPI server
uvicorn main:app --reload

Swagger UI: http://localhost:8000/docs
Custom Swagger UI: http://localhost:8000/custom-docs


 ## API Key Authentication

All routes require a valid API key.

Include this header in every request:
x-api-key: math123secret
In Swagger UI:
Click the "Authorize" button (top-right)

Paste the API key: math123secret


##📬 API Endpoints
##➕ POST /power
Calculates x raised to the power of y
Query parameters: x, y

##🧾 GET /power/history
Returns history of all power operations

##➕ POST /factorial
Calculates the factorial of x
Query parameter: x

##🧾 GET /factorial/history
Returns history of all factorial operations

##➕ POST /fibonacci
Calculates the n-th Fibonacci number
Query parameter: x

##🧾 GET /fibonacci/history
Returns history of all Fibonacci operations

##📄 GET /
Returns a welcome message with documentation links

##📄 GET /custom-docs
Loads an alternative Swagger UI with a custom favicon

##🗃️ Data Persistence
All operations are stored in a SQLite database file math_ops.db

##Schema:

operation (e.g. power)

x, y, result, timestamp

##📝 Logging
Every operation is recorded in math_api.log

Fibonacci operations include [CACHE HIT] entries when results are reused from cache

##🛠 Tech Stack
Python 3.11
FastAPI
SQLite3
Uvicorn (development server)
Pydantic

Logging (Python standard
