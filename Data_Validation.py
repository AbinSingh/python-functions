
from pydantic import BaseModel

class data_validation(BaseModel):
    salary : int
    name : str
    age : int

def employee_profile(salary, name, age):
    print(f'salary is {salary}')
    print(f'name is {name}')
    print(f'age is {age}')

if __name__ == "__main__":
    employee_details = {'salary': 2500, 'name': 'abin', 'age': 26}
    try:
        data_validation(**employee_details)
    except Exception as e:
        print(e)
    else:
        employee_profile(**employee_details)


