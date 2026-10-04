from pydantic import BaseModel,Field
from fastapi import FastAPI


# Field Validation
class Item(BaseModel):
    name : str = Field(...,min_length=1,max_length=100)
    description:str | None = Field(None,max_length=500) 
    price:float = Field(...,gt = 0) # Greater than 0 
    tax : float = Field(None,ge = 0) # Freater than or equals to 0


#  Post the items to the Server 
app  = FastAPI("Data Validation")


@app.post("/items/")
def create_items(items:Item):
    return items


