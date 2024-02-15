from fastapi import FastAPI
app = FastAPI()

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