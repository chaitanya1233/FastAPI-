# Request Body - Following the Official FastAPI Tutorial
# Learn how to handle POST requests with data in the request body

from fastapi import FastAPI
# TODO: Import BaseModel from pydantic

app = FastAPI()

# Step 1: Create a Pydantic model (from official tutorial)
# TODO: Create a class called 'Item' that inherits from BaseModel
# TODO: Add these fields:
#   - name: str
#   - description: str | None = None
#   - price: float
#   - tax: float | None = None

from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description:str | None = None
    price : float
    tax : float | None = None

# Step 2: Use the model in a POST endpoint
# TODO: Create a POST endpoint at "/items/"
# TODO: Add parameter: item: Item
# TODO: Return the item (FastAPI will serialize it automatically)

@app.post("/items/")
async def create_items(items:Item):
    return items

# Step 3: Use the model with additional data
# TODO: Create a POST endpoint at "/items/{item_id}"
# TODO: Add path parameter: item_id: int
# TODO: Add body parameter: item: Item
# TODO: Return: {"item_id": item_id, **item.dict()}

@app.post("/items/{item_id}")
async def create_items(item_id:int,item:Item):
    return {"item_id":item_id, **item_dict()}