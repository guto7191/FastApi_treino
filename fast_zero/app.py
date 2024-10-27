from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message' : 'Olá Mundo!'}
