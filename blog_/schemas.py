from pydantic import BaseModel
from typing import List
from . import models, schemas

class Faculty(BaseModel):
    f_name: str

class Student(BaseModel):
    s_name: str
    roll_no: str
    F_id: int

