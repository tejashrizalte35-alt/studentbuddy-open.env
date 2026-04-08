from pydantic import BaseModel
from typing import List, Optional
class Task:
    def __init__(self, title, completed=False, deadline=0):
        self.title = title
        self.completed = completed
        self.deadline = deadline

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
