from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from typing import List

from models import OperationRequest, OperationResponse, OperationRecord
from services import MathService
from db import SQLiteDatabase
from logger import LoggerService

# === API Key config ===
API_KEY = "math123secret"
API_KEY_NAME = "x-api-key"

def verify_api_key(x_api_key: str = Header(...)) -> None:
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API Key.")

# === Init app and DB ===
db = SQLiteDatabase()

app = FastAPI(
    title="Math Microservice API",
    description=(
        "API for individual mathematical operations: power, factorial, and Fibonacci.\n\n"
        "**Authentication required:** use header `x-api-key: math123secret`"
    ),
    version="1.0.0",
    contact={
        "name": "Ioana Zinveliu",
        "email": "ioana-victoria.zinveliu@endava.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# === Swagger Auth ===
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "APIKeyHeader": {
            "type": "apiKey",
            "in": "header",
            "name": API_KEY_NAME
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"APIKeyHeader": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# === General ===

@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Welcome to the Math Microservice API.",
        "docs": "/docs",
        "custom_docs": "/custom-docs"
    }

@app.get("/custom-docs", include_in_schema=False)
def custom_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Custom Math Swagger UI",
        swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png"
    )

# === Power ===

@app.post("/power", response_model=OperationResponse, tags=["Power"])
def compute_power(x: int, y: int, _: None = Depends(verify_api_key)) -> OperationResponse:
    """Calculate x raised to the power of y."""
    try:
        result = MathService.pow_fn(x, y)
        db.save_operation("power", x, y, result)
        LoggerService.log_operation("power", x, y, result)
        return OperationResponse(result=result, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/power/history", response_model=List[OperationRecord], tags=["Power"])
def power_history(_: None = Depends(verify_api_key)) -> List[OperationRecord]:
    """Retrieve history of all power operations."""
    return [op for op in db.get_all_operations() if op["operation"] == "power"]

# === Factorial ===

@app.post("/factorial", response_model=OperationResponse, tags=["Factorial"])
def compute_factorial(x: int, _: None = Depends(verify_api_key)) -> OperationResponse:
    """Calculate factorial of x."""
    try:
        result = MathService.factorial(x)
        db.save_operation("factorial", x, 0, result)
        LoggerService.log_operation("factorial", x, None, result)
        return OperationResponse(result=result, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/factorial/history", response_model=List[OperationRecord], tags=["Factorial"])
def factorial_history(_: None = Depends(verify_api_key)) -> List[OperationRecord]:
    """Retrieve history of all factorial operations."""
    return [op for op in db.get_all_operations() if op["operation"] == "factorial"]

# === Fibonacci ===

@app.post("/fibonacci", response_model=OperationResponse, tags=["Fibonacci"])
def compute_fibonacci(x: int, _: None = Depends(verify_api_key)) -> OperationResponse:
    """Calculate the n-th Fibonacci number."""
    try:
        result = MathService.fibonacci(x)
        db.save_operation("fibonacci", x, 0, result)
        LoggerService.log_operation("fibonacci", x, None, result)
        return OperationResponse(result=result, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fibonacci/history", response_model=List[OperationRecord], tags=["Fibonacci"])
def fibonacci_history(_: None = Depends(verify_api_key)) -> List[OperationRecord]:
    """Retrieve history of all Fibonacci operations."""
    return [op for op in db.get_all_operations() if op["operation"] == "fibonacci"]
