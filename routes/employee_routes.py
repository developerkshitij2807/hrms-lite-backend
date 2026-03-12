from fastapi import APIRouter
from database import employee_collection
from models.employee import Employee

router = APIRouter()

@router.post("/employees")
def add_employee(employee: Employee):
    employee_collection.insert_one(employee.dict())
    return {"message": "Employee added"}

@router.get("/employees")
def get_employees():
    employees = list(employee_collection.find({}, {"_id": 0}))
    return employees

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: str):
    employee_collection.delete_one({"employeeId": employee_id})
    return {"message": "Employee deleted"}