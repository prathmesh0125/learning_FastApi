from fastapi  import FastAPI, Form ,File,UploadFile,HTTPException
app= FastAPI()
from typing import Union
from enum import Enum
from pydantic import BaseModel
# model
class Choice_name(str,Enum):
   one="one"
   two="two" 
   three="three"

# schema
class schema1(BaseModel):
   name:str
   Clas:str
   roll_no:int
     
# simple routes
@app.get("/")
async def root():
   return {"message":"hello world"}
# simple routes
@app.get("/h")
async def root():
   return {"msg":"hey"}

# path parameter
@app.get('/item/{Item}')
def path_func(Item):
   var_name={"path variable":Item}
   return var_name

# query parameter

# @app.get('/query/')
# def quer_func( roll_no:int,name:Union[str,None]=None):
#    var_nam={"name":name,"roll no":roll_no}
#    return (var_nam)

@app.get('/query')
def quer_func(name: str, roll_no: Union[int, int] = 100):
    var_nam = {"name": name, "roll no": roll_no}
    return var_nam


@app.get("/models/{model_name}")
async def get_model(model_name:Choice_name):
   return (model_name)

# Response body
@app.post("/items/")
async def create_item(item:schema1):
   return (item)

# form data
@app.post('/form/data/')
async def form_data(username:str=Form(),password:str =Form()):
   return ({"username":username,"password":password})
 
# file upload
# file lenght
@app.post("/file/length")
async def file_lenght(file:bytes = File()):
    return {"file": len(file)}
 
#  file upload
@app.post("/file/upload")
async def file_upload(file: UploadFile):
    return {"file-name": file.filename,"content":file.content_type}
 
# error handling
@app.get("/error/handling")
async def handle_error(item:int):
   if item==2:
      return HTTPException(status_code=400,detail="item is not equal to 2 try anothe value") 
   return{"value":item}

items=[1,2,3,4,5]
@app.get('/error/value')
async def value_present(number:int):
  if number not in items:
     return HTTPException(status_code=400,detail="value is not present in array")
  return {"value":number}