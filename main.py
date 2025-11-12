from fastapi import FastAPI
from models import NumbersInput, SumResponse, SubtractResponse

app = FastAPI(
<<<<<<< HEAD
    title="Operations Calculator API",
    description="API to calculate mathematical operations with two numbers",
=======
    title="Calculator API",
    description="API to calculate operations of two numbers",
>>>>>>> main
    version="1.0.0"
)


@app.get("/")
def read_root():
    """
    Welcome endpoint with API information.
    """
    return {
        "message": "Hello! Welcome to the Operations Calculator API",
        "description": "This API calculates mathematical operations with two numbers",
        "endpoints": {
            "POST /api/sum": "Calculate the sum of two numbers",
            "POST /api/subtract": "Calculate the difference of two numbers"
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


@app.post("/api/subtract", response_model=SubtractResponse)
def calculate_subtract(numbers: NumbersInput):
    """
    Calculate the difference of two numbers.

    - **first_number**: The number to subtract from (minuend)
    - **second_number**: The number to subtract (subtrahend)

    Returns a JSON response with both input numbers and their difference.
    """
    result = numbers.first_number - numbers.second_number
    return SubtractResponse(
        first_number=numbers.first_number,
        second_number=numbers.second_number,
        difference=result
    )
