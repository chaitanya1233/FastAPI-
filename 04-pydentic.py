from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name : str
    description : str | None = None
    price : float 
    tax : float | None = None


@app.post("/items/")
def create_item(item:Item):
    return item


# Example 2 : request Body + Path parameters 

app.post("/items/{item_id}")
def create_item_id(item_id:int,item:Item):
    return {"item_id":item_id,**item.dict()}


# Example 3: Request Body + Path + Query Parameters

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

