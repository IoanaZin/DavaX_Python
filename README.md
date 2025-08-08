#  Math Microservice API – FastAPI + SQLite

##  Overview

This project is a lightweight **RESTful microservice** built with **FastAPI**, offering three core mathematical operations:

- `power`: computes `x^y`
- `factorial`: computes `n!`
- `fibonacci`: computes the n-th Fibonacci number

Each operation has its own **POST endpoint** and corresponding **GET endpoint** for viewing operation history.  
Results are saved to a **SQLite database**, and operations are logged in a `.log` file.

>  **Authentication required**: use header `x-api-key: math123secret` in all requests.

---

##  Project Structure

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


### General Architecture
This project is designed as a lightweight microservice using FastAPI to expose mathematical operations via RESTful API endpoints. It is structured according to clean, modular principles:

-FastAPI handles routing, validation, and documentation

-SQLite is used for local data persistence (no server required)

-Pydantic validates input/output models

-Logging is used to record all operations and cache hits

 ### File Responsibilities
🔹 main.py
This is the entry point of the app.

Initializes the FastAPI application with full metadata (title, description, version, license, contact).

Defines all routes:

POST routes: /power, /factorial, /fibonacci

GET routes: /power/history, /factorial/history, /fibonacci/history, /, /custom-docs

Secures all endpoints using a custom API key (x-api-key).

Uses FastAPI’s dependency injection to enforce security.

🔹 services.py
Contains the MathService class which handles mathematical computations:

pow_fn(x, y) — exponentiation

factorial(n) — iterative factorial

fibonacci(n) — iterative Fibonacci with memoization

Implements caching for Fibonacci and logs cache hits via LoggerService.

🔹 models.py
Defines Pydantic models:

OperationRequest: structure for input data

OperationResponse: structure for standard API responses

OperationRecord: format for records retrieved from the database

🔹 db.py
Contains the SQLiteDatabase class responsible for:

Connecting to the math_ops.db file

Creating the operations table if it doesn’t exist

Inserting new operations

Retrieving all records (used for history endpoints)

🔹 logger.py
Contains the LoggerService class used to log operations.

Logs all operations to a file math_api.log.

Logs [CACHE HIT] messages for Fibonacci when results are reused.
---

##  How to Run Locally

### 1. Clone the project and set up the environment

git clone https://github.com/IoanaZin/DavaX_Python_homework.git
cd DavaX_Python_homework
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -r requirements.txt


### 2. Start the FastAPI server

uvicorn main:app --reload
Swagger UI: http://localhost:8000/docs

Custom Swagger UI: http://localhost:8000/custom-docs

##  API Key Authentication
All endpoints are protected with an API key.

Required header
x-api-key: math123secret
In Swagger UI
Click Authorize (top right)

Paste the key: math123secret

Click Authorize

##  API Endpoints

➕ POST /power
Description: Calculates x^y

Params: x, y

🧾 GET /power/history
Returns history of all power operations

➕ POST /factorial
Description: Calculates factorial of x

Param: x

🧾 GET /factorial/history
Returns history of all factorial operations

➕ POST /fibonacci
Description: Calculates the n-th Fibonacci number

Param: x

🧾 GET /fibonacci/history
Returns history of all Fibonacci operations

📄 GET /
Welcome message with helpful links

📄 GET /custom-docs
Alternative Swagger UI with custom favicon

## 🗃 Data Persistence
All results are saved in a local SQLite database (math_ops.db)

Schema:
operation (e.g. power)

x, y

result

timestamp

##  Logging
Every operation is recorded in math_api.log

Fibonacci operations log [CACHE HIT] when results are retrieved from cache

##  Tech Stack
Python 3.11

FastAPI

SQLite

Pydantic

Uvicorn

Python logging module
