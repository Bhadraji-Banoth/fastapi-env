from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

class Student(BaseModel):
    name:str
    gender:str
    marks:int