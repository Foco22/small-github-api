from pydantic import BaseModel, Field


class NumbersInput(BaseModel):
    """Request model for sum calculation"""
    first_number: float = Field(..., description="The first number to add")
    second_number: float = Field(..., description="The second number to add")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_number": 5.0,
                    "second_number": 3.0
                }
            ]
        }
    }


class SumResponse(BaseModel):
    """Response model for sum calculation"""
    first_number: float = Field(..., description="The first number that was added")
    second_number: float = Field(..., description="The second number that was added")
    sum: float = Field(..., description="The result of the addition")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_number": 5.0,
                    "second_number": 3.0,
                    "sum": 8.0
                }
            ]
        }
    }


class SubtractResponse(BaseModel):
    """Response model for subtract calculation"""
    first_number: float = Field(..., description="The first number (minuend)")
    second_number: float = Field(..., description="The second number (subtrahend)")
    difference: float = Field(..., description="The result of the subtraction")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_number": 10.0,
                    "second_number": 3.0,
                    "difference": 7.0
                }
            ]
        }
    }
