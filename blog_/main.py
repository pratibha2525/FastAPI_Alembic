from fastapi import FastAPI, Depends, status, Response, HTTPException
from . schemas import Faculty
from . import schemas, models
from .database import engine, sessionlocal
from sqlalchemy.orm import Session 


app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = sessionlocal()

    try:
        yield db
    finally:
        db.close()

################# Faculty_CRUD

@app.post('/faculty', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Faculty, db: Session = Depends(get_db)):
    new_faculty = models.Faculty(f_name=request.f_name)
    db.add(new_faculty)
    db.commit()
    db.refresh(new_faculty)
    return new_faculty

@app.get('/faculty')
def all(db: Session = Depends(get_db)):
    faculty = db.query(models.Faculty).all()
    return faculty

@app.get('/faculty/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
    faculty = db.query(models.Faculty).filter(models.Faculty.id == id).first()
    if not faculty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Faculty with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Faculty with the id {id} is not available"}
    return faculty

@app.delete('/faculty/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    faculty = db.query(models.Faculty).filter(models.Faculty.id == 
                                id).delete(synchronize_session=False)
    db.commit()
    return 'done'


@app.put('/faculty/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Faculty, db: Session = Depends(get_db)):

    faculty = db.query(models.Faculty).filter(models.Faculty.id == id)

    if not faculty.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = f"Faculty with the id {id} is not found")
    faculty.update({'f_name': request.f_name})
    db.commit()
    return "Updated"

################ Student_CRUD

@app.post('/student', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Student, db: Session = Depends(get_db)):
    new_student = models.Student(s_name=request.s_name, roll_no=request.roll_no,F_id=request.F_id)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get('/student')
def all(db: Session = Depends(get_db)):
    student = db.query(models.Student).all()
    return student

@app.get('/student/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with the id {id} is not available")
    return student

@app.put('/student/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Student, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(models.Student.id == id)

    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = f"Student with the id {id} is not found")
    student.update({'s_name': request.s_name,'s_subject': request.s_subject, 'roll_no': request.roll_no })
    db.commit()
    return "Updated"

@app.delete('/student/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == 
                                id).delete(synchronize_session=False)
    db.commit()
    return 'done'

########### Get faculty id, show perticuler faculty student ...

@app.get('/std/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(models.Student.F_id == id).all()
    faculty = db.query(models.Faculty).filter(models.Faculty.id == id).first()
    f =(faculty.f_name)
    return {'student':student,'faculty':f}