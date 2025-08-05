from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import models
import crud
import schema
from database import engine,Sessionlocal
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependcy for Database session

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/insert", response_model=schema.Student)
def create_student(student: schema.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/retrieve", response_model=List[schema.Student])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.put("/update/{sid}", response_model=schema.Student)
def update_student(sid: int, student: schema.StudentCreate, db: Session = Depends(get_db)):
    updated = crud.update_student(db, sid, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@app.delete("/delete/{sid}")
def delete_student(sid: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db, sid)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Deleted successfully"}





















