from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Start the server: uvicorn users:app --reload

# User Entity


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


users_list = [
    User(id=1, name="Bautista", surname="Prieto", age=15),
    User(id=2, name="Tomas", surname="Gonzalez", age=21),
    User(id=3, name="Lorenzo", surname="GoodNews", age=19),
]


@app.get("/users")
async def usersJson():
    return [
        {
            "id": 1,
            "name": "Bautista",
            "surname": "Prieto",
            "age": 15
        }, {
            "id": 2,
            "name": "Tomas",
            "surname": "Gonzalez",
            "age": 21
        }, {
            "id": 3,
            "name": "Lorenzo",
            "surname": "GodNEWs",
            "age": 19
        }
    ]


@app.get("/users")
async def users():
    return users_list

# With Path
# http://127.0.0.1:8000/with_path/2


@app.get("/with_path/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "That id doesn't exist!"

# With Query
# http://127.0.0.1:8000/with_query/?id=1


@app.get("/with_query/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "That id doesn't exist!"


@app.post("/user/")
async def add(user: User):
    if type(search_user(user.id)) == User:
        return {"msg": "User already exist"}
    else:
        users_list.append(user)


@app.put("/users")
async def user(user: User):
    found = False

    for i, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[i] = user
            found = True

    if not found:
        return {"Error": "User Not Found."}
    else:
        return user


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return users[0]
    except:
        return {"FatalError": "User not found"}


@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for i, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[i]
            found = False

    if not found:
        return {"Error": "User Not Found."}
