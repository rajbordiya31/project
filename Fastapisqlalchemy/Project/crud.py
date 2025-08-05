from sqlalchemy.orm import Session
import models
import schema

def create_student(db:Session,student:schema.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db:Session):
    return db.query(models.Student).all()

def update_student(db:Session,sid:int,student:schema.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == sid).first()
    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.mob = student.mob
        db.commit()
        db.refresh(db_student)
    return db_student
def delete_student(db: Session, sid: int):
    db_student = db.query(models.Student).filter(models.Student.id == sid).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student




