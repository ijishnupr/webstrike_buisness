from fastapi import FastAPI

app = FastAPI()

@app.get("/api/auth/login")
async def route():
    return {"message": "Hello, World!"}