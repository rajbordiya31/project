from pydantic import BaseModel

# Input ke liye (create/update)
class StudentBase(BaseModel):
    name: str
    age: int
    mob: str
# Create ke liye
class StudentCreate(StudentBase):
    pass

# Response (output) ke liye
class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
