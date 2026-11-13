from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Hi My name is Praveen"


greet()