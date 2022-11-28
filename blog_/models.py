from sqlalchemy import Column, Integer, String
from .database import Base
# from sqlalchemy.orm import relationship


class Faculty(Base):
    __tablename__ = 'faculty'

    id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String)


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    s_name = Column(String)
    roll_no = Column(Integer)
    F_id = Column(Integer)



