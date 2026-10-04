# Query Parameters - Following the Official FastAPI Tutorial
# Learn how to handle optional parameters in URLs

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Step 1: Create an endpoint with query parameters
# TODO: Create a GET endpoint at "/items/"
# TODO: Add function parameters: skip: int = 0, limit: int = 10
# TODO: Return the slice fake_items_db[skip : skip + limit]
# Hint: Function parameters become query parameters automatically!
@app.get("/items/")
async def read_items(skip:int = 0,limit: int = 10):
    return fake_items_db[skip:skip+limit]


# Step 2: Combine path and query parameters (from official tutorial)
# TODO: Create a GET endpoint at "/items/{item_id}"
# TODO: Add path parameter: item_id
# TODO: Add query parameter: q: str | None = None
# TODO: Return {"item_id": item_id, "q": q} when q was given,
#       and {"item_id": item_id} when it was not
# Hint: Mix path parameters {item_id} with query parameters q

@app.get("/items/{item_id}")
def read_items(item_id:str,q:str |None = None):
    if q:
        return {"item_id":item_id,"q":q}
    return {"item_id":item_id}


@app.post("/items/")
async def add_item(item: dict):
    fake_items_db.append(item)
    return fake_items_db