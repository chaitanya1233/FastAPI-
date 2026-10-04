from fastapi import FastAPI

app  = FastAPI("String Validation")


# 1. Basic Query 
@app.get("/items/")
def read_items(q:str | None = None):
    return {"q":q}


# 2. Advanced approach with query

from fastapi import Query

@app.get("/items/")
def read_items(q:str | None = Query(default=None,max_length=50)):
    return {"q":q}


# The Query Function
# The Query function allows you to add metadata and validation constraints to query parameters.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Basic Query Usage
@app.get("items")
def read_items(q:str | None = Query(default=None,max_length=50))
    result = []
    if q :
        # Filter items based on query
        result = [item for item in fake_items_db if q.lower() in item["item_name"].lower()]

    else:
        result = fake_items_db
    return {"result":result}



