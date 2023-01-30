import azure.functions as func
import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = func.FunctionApp()
fast_app = FastAPI()


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


@fast_app.get("/item/{item_id}", response_model=Item, responses={404: {"model": Message}})
async def getitem(item_id: str):
    if item_id == "1":
        return Item(id="1", value="Some Item")
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
        

app = func.AsgiFunctionApp(app=fast_app, http_auth_level=func.AuthLevel.ANONYMOUS)



