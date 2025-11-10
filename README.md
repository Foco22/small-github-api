# Operations Numbers APIs

This API makes calculations.

## Endpoints

### GET /
Welcome endpoint with API information.

### POST /api/sum
Calculate the sum of two numbers.

**Request body:**
```json
{
  "first_number": 5,
  "second_number": 3
}
```

**Response:**
```json
{
  "first_number": 5,
  "second_number": 3,
  "sum": 8
}
```
