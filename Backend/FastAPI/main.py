from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Start the server: uvicorn main:app --reload

@app.get("/")
async def root():
    return "¡Hello FastAPI!"

@app.get("/url")
async def json():
    return {
    "Name": "Bautista",
    "Surname": "Prieto",
    "Age": 15,
    "Skills": {
        "Frontend": [
            "JavaScript",
            "CSS",
            "HTML",
            "React"
        ],
        "Backend": [
            "Python",
            "Rust"
        ]
    }
}