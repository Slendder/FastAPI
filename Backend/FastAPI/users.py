from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

# Entidad User


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


users_list = [
    User(id=1, name="Bautista", surname="Prieto", age=15),
    User(id=2, name="Tomas", surname="Gonzalez", age=21),
    User(id=3, name="Lorenzo", surname="BuenaNueva", age=19),
]


@app.get("/usersjson")
async def usersJson():
    return [
        {
            "name": "Bautista",
            "surname": "Prieto",
            "age": 15
        }, {
            "name": "Tomas",
            "surname": "Gonzalez",
            "age": 21
        }, {
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

