# 🔢 Math Microservice API – FastAPI + SQLite

## 🧠 Overview

This project is a lightweight **RESTful microservice** built with **FastAPI**, offering three core mathematical operations:

- `power`: computes `x^y`
- `factorial`: computes `n!`
- `fibonacci`: computes the n-th Fibonacci number

Each operation has its own **POST endpoint** and corresponding **GET endpoint** for operation history.  
Results are saved to a **SQLite database** and operations are logged to a `.log` file.

> 🔐 **Authentication required**: Use header `x-api-key: math123secret` in all requests.

---

## 📁 Project Structure

math_api/
├── main.py # FastAPI app and routes

├── services.py # MathService with operation logic

├── db.py # SQLiteDatabase for saving history

├── logger.py # LoggerService for writing logs

├── models.py # Pydantic models for request/response

├── math_ops.db # SQLite database (auto-generated)

├── math_api.log # Log file (auto-generated)

├── requirements.txt # Python dependencies

├── README.md # Project documentation

---

## 🚀 How to Run Locally

### 1. Clone the project and set up the environment

```bash
git clone https://github.com/IoanaZin/DavaX_Python_homework.git
cd DavaX_Python_homework
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
### 2. Start the FastAPI server
uvicorn main:app --reload
Swagger UI: http://localhost:8000/docs

Custom Swagger UI: http://localhost:8000/custom-docs

🔐 API Key Authentication
All endpoints are protected with an API key.

Required header:
x-api-key: math123secret
In Swagger UI:
Click Authorize (top right)

Paste the key math123secret

Click Authorize again

📬 API Endpoints
➕ POST /power
Description: Calculates x raised to the power of y

Params: x, y

🧾 GET /power/history
Returns all power operations

➕ POST /factorial
Description: Calculates the factorial of x

Param: x

🧾 GET /factorial/history
Returns all factorial operations

➕ POST /fibonacci
Description: Calculates the n-th Fibonacci number

Param: x

🧾 GET /fibonacci/history
Returns all Fibonacci operations

📄 GET /
Welcome message + useful links

📄 GET /custom-docs
Alternative Swagger UI with favicon

🗃️ Data Persistence
All results are saved in a local SQLite database (math_ops.db)

Each record includes:

operation (e.g. power)

x, y

result

timestamp

📝 Logging
Every operation is logged in math_api.log

Fibonacci includes [CACHE HIT] log lines when reused

🛠 Tech Stack
Python 3.11

FastAPI

SQLite

Pydantic

Uvicorn

Python logging module


- `test_main.py` for testing endpoints

I'm here to help!
