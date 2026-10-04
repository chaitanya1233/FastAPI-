from fastapi import FastAPI


from enum import Enum
from pydantic import BaseModel,Field
from fastapi import HTTPException

app  = FastAPI(title = "Task Board")


#  Step 4 : 
class TaskStatus(str,Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskCreate(BaseModel):
    title : str = Field(...,min_length=3,max_length=100)
    status : TaskStatus = TaskStatus.todo




# Step 1: The front door
@app.get("/")
def root():
    return {"message":"Welocme to Task Board!"}


# Step 2: The shelf and the list endpoint

tasks = [
    {"id":1,"title":"Learn rounting","status":"done"},
    {"id":2,"title":"Learn Validation","status":"done"},
    {"id":3,"title":"Build the Task Board","status":"in_progress"},
]


@app.get('/tasks')
def list_tasks(skip:int = 0,limit : int = 10):
    return tasks[skip : skip+limit]


# Test these in the browser:

# /tasks
# /tasks?limit=2
# /tasks?skip=1&limit=1
# /tasks?limit=abc (what error do you get, and why?)


# Step 3: Get one task (new tool: HTTPException)

from fastapi import HTTPException



@app.get('/tasks/status')
def status():
    return {"total":len(tasks)}


@app.get("/tasks/status/{task_id}")
def get_tasks(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404,detail="Task not found!")


# Step 4 :Create a task (Pydantic + Field)

#  Check top of main.py for difination

# placement doesn't matter here, because POST /tasks has no path parameter


@app.post("/tasks",status_code=201)
def create_task(task:TaskCreate):
    new_task = {
        "id":len(task)+1,
        "title":task.title,
        "status" : task.status, 
    }

    task.append(new_task)
    return new_task



 

