from fastapi import FastAPI

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
app = FastAPI()


@app.get("/")
def read_root():
    return {'message' : 'Olá Mundo!'}
