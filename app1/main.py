from fastapi import FastAPI
# from sqlalchemy.orm import Session
# from typing import List
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def checking():
    return {"message": "hello"}
