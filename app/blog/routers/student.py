from typing import List
from fastapi import APIRouter,Depends
from blog import schemas, database, models
from sqlalchemy.orm import Session

router=APIRouter()

get_db=database.get_db

@router.post('/student', tags=["Students"])
def create(request:schemas.Student,db:Session=Depends(get_db)):
    new_student=models.Student(name=request.name, gender=request.gender, marks=request.marks)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student