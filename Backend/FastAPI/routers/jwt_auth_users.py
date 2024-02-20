from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(shemes=["bcrypt"])


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "johnsmith": {
        "username": "johnsmith",
        "full_name": "John Smith",
        "email": "john.smith@example.com",
        "disabled": False,
        "password": "$2a$12$MPlqMDTW5nI/e67tMSCMeeo61Mu7TGEOywZU3TJY3PRpH58iPGrEa"
    },
    "alicemiller": {
        "username": "alicemiller",
        "full_name": "Alice Miller",
        "email": "alice.miller@example.com",
        "disabled": True,
        "password": "$2a$12$8rFNag5N03jykIvErXI9guG7CLAvO2l98Ld8/KAGC5zq/WDZNh47O"
    },
    "jdoe": {
        "username": "jdoe",
        "full_name": "Jane Doe",
        "email": "jane.doe@example.com",
        "disabled": False,
        "password": "$2a$12$uNxyKF6fgaQwc1Wka6pnV.Lq4akykFsV5dVoZhQ.FsItz7Cs7BNbW"
    },
    "guest": {
        "username": "guest",
        "full_name": "Guest user",
        "email": "nobody@nowhere.com",
        "disabled": True,
        "password": "$2a$12$8JCqmJOKa52McQcdr/2h3eXoOytuy0Ufe./oyWVmnqECVrlUwDiIq"
    }
}


def search_user_DB(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username")

    user = search_user_DB(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

    return {"access_token": user.username,  "token_type": "bearer"}
