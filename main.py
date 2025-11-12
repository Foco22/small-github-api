from fastapi import FastAPI
from models import NumbersInput, SumResponse

app = FastAPI(
    title="Calculator API",
    description="API to calculate operations of two numbers",
    version="1.0.0"
)


@app.get("/")
def read_root():
    """
    Welcome endpoint with API information.
    """
    return {
        "message": "Hello! Welcome to the Sum Calculator API",
        "description": "This API calculates the sum of two numbers",
        "endpoints": {
            "POST /api/sum": "Calculate the sum of two numbers"
        },
        "documentation": "/docs"
    }


@app.post("/api/sum", response_model=SumResponse)
def calculate_sum(numbers: NumbersInput):
    """
    Calculate the sum of two numbers.

    - **first_number**: The first number to add
    - **second_number**: The second number to add

    Returns a JSON response with both input numbers and their sum.
    """
    result = numbers.first_number + numbers.second_number
    return SumResponse(
        first_number=numbers.first_number,
        second_number=numbers.second_number,
        sum=result
    )
