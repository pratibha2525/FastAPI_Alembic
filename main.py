from fastapi import FastAPI
from models import Faculty


app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'kitty'}}

@app.get('/blog/{id}')
def show():
    return {'data':id}

@app.post('/faculty')
def create_blog(request: Faculty):
    return request
    return {'data': "Faculty is created"}

    