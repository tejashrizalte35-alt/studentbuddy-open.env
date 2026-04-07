from pydantic import BaseModel
from typing import List, Optional

# 1. Update Task to be a BaseModel
class Task(BaseModel):
    title: str
    deadline: int
    priority: int
    task_type: str = "assignment"
    completed: bool = False

# Now Pydantic can successfully generate the schema for this list
class Observation(BaseModel):
    tasks: List[Task]
    time_left: int
    stress: float

class Action(BaseModel):
    action_type: str  # schedule / complete / rest
    task_title: str = ""
    time_spent: int = 0

class Reward(BaseModel):
    value: float