from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


users_db = {
    "johnsmith": {
        "username": "johnsmith",
        "full_name": "John Smith",
        "email": "john.smith@example.com",
        "disabled": False,
        "password": "123456"
    },
    "alicemiller": {
        "username": "alicemiller",
        "full_name": "Alice Miller",
        "email": "alice.miller@example.com",
        "disabled": True,
        "password": "654321"
    },
    "jdoe": {
        "username": "jdoe",
        "full_name": "Jane Doe",
        "email": "jane.doe@example.com",
        "disabled": False,
        "password": "14fasf"
    },
    "guest": {
        "username": "guest",
        "full_name": "Guest user",
        "email": "nobody@nowhere.com",
        "disabled": True,
        "password": "jaufusa"
    }
}


class UserDB(User):
    password: str


def search_user_DB(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username")

    user = search_user_DB(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
