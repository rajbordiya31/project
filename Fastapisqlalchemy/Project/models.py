from database import Base
from sqlalchemy import Column,Integer,String

class Student(Base):
    __tablename__ = "studentinfo"

    id = Column(Integer,primary_key=True)
    name =Column(String(100))
    age=Column(Integer)
    mob = Column(String(100))


