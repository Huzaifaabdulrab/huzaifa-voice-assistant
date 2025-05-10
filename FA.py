from fastapi import FastAPI
from pydantic import BaseModel
from main import run_assistant

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Assistant Sever Running "}

@app.post('/start')
def start_assistant():
    return {"message" : "Assistant started"}

class Command(BaseModel):
    command : str

@app.post("/command")
def send_command(cmd:Command):
    return {"status": "received" , "comand" : cmd.command }