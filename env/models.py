from pydantic import BaseModel
from typing import List, Optional
class Task(BaseModel):
    title: str
    completed: bool
    deadline: int
    priority: int = 1   
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
