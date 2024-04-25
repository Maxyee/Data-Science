from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello world 2"}


@app.post("/")
async def post():
    return {"message" : "hello from post method route"}


@app.put("/")
async def put():
    return {"message": "hello from put method route"}

