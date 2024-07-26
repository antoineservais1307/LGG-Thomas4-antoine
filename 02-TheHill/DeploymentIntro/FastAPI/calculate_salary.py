def calculate_salary(salary, bonus, taxes):
    # Check if all inputs are of numeric type (int or float)
    if not all(isinstance(i, (int, float)) for i in [salary, bonus, taxes]):
        print("Error: must input integers or floats")
        return None

    # Calculate the final salary
    final_salary = salary + bonus - taxes
    return final_salary

