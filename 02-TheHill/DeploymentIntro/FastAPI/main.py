from fastapi import FastAPI
from pydantic import BaseModel
from calculate_salary import calculate_salary

class User_input(BaseModel):
    salary : float
    bonus : float
    taxes : float

app = FastAPI()

@app.post("/calculate_salary")
def operate(input:User_input):
    result = calculate_salary(input.salary , input.bonus, input.taxes)
    return result