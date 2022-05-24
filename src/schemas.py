from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str

class Employee(EmployeeBase):
    emp_id: int
    class Config:
        orm_mode = True

class EmployeeCreate(EmployeeBase):
    class Config:
        orm_mode = True