from fastapi import FastAPI

app = FastAPI(title="First FastAPI Application")

@app.get("/") # This creates a path opration : / --> root path 
async def root():
    return {"messages":"Hello World!"}


# GET : The HTTP method
# root() : Python function that handels requests 

# The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to:

# The path /
# Using a GET operation


# Path operation ?

# 🌐 What is a "Path Operation"?
# A path operation is one of these HTTP methods:

# GET: To read data
# POST: To create data
# PUT: To update data
# DELETE: To delete data
# ...and a few more


#  In HTTP protocol you communicate using one of these
# Protocols 

