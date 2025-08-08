from pydantic import BaseModel, Field
from typing import Optional


class OperationRequest(BaseModel):
    """
    Request model received from the user for a mathematical operation.

    Fields:
    - operation: type of operation ('power', 'factorial', 'fibonacci')
    - x: main input value (base or operand)
    - y: optional second value (required for 'power')
    """
    operation: str = Field(..., example="power")
    x: int = Field(..., example=2)
    y: Optional[int] = Field(None, example=3)


class OperationResponse(BaseModel):
    """
    Response model returned to the user after computation.

    Fields:
    - result: computed integer result
    - status: message indicating operation success
    """
    result: int = Field(..., example=8)
    status: str = Field(..., example="success")


class OperationRecord(BaseModel):
    """
    Model representing a stored mathematical operation from the database.

    Fields:
    - operation: operation type
    - x: input value
    - y: optional second input (if applicable)
    - result: computed result
    - timestamp: ISO 8601 timestamp of operation
    """
    operation: str
    x: int
    y: Optional[int] = None
    result: int
    timestamp: str
