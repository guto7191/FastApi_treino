from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchame(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(UserSchame):
    id: int


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]
