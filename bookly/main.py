from fastapi import FastAPI, Header

from typing import Optional

from pydantic import BaseModel

app = FastAPI()


# route
@app.get("/")
async def root_body():
    return {"msg": "hello"}


# path parameter


@app.get("/greet/{name}")
async def greeting(name: str):
    return {"msg": f"hello {name}"}


# path + query parameter


@app.get("/greeting/{name}")
async def greet(name: str, age: int):
    return {"msg": f"hello {name}", "age": age}


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {"title": book_data.title, "author": book_data.author}


# get headrs
@app.get("/get_headers")
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headres={}
    
    request_headres["Accept"]=accept
    request_headres["content-Type"]=content_type
    request_headres["user-Agent"]=user_agent
    request_headres["Host"]=host
    
    return request_headres
