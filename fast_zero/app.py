from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchame

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
app = FastAPI()

data_base = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchame):
    user_with_id = UserDB(id=len(data_base) + 1, **user.model_dump())

    data_base.append(user_with_id)

    return user_with_id


@app.get("/users/", response_model=UserList)
def read_users():
    return {"users": data_base}
