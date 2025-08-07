from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "studentinfo"

    id = Column(Integer,primary_key=True)
    name =Column(String(100))
    age=Column(Integer)
    mob = Column(String(100))

    user = relationship("User",back_populates="student")

# class User(Base):
#     __tablename__ = "user"
    
#     id = Column(Integer,primary_key=True,index=True)
#     username =Column(String(100),index=True,unique=True)
#     hash_password = Column(String)
#     Student_id = Column(Integer,ForeignKey("studentinfo.id"))
#     student = relationship("Student",back_populates="user")
    

