from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    employeeId: str
    fullName: str
    email: EmailStr
    department: str