from fastapi import FastAPI, Request
from env.environment import StudentEnv
from env.models import Action

app = FastAPI()
env = StudentEnv()

# This is where you put the app.post for the evaluator
@app.post("/reset")
async def reset():
    obs = env.reset()
    # The evaluator expects the state/observation back
    return obs 

@app.post("/step")
async def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

@app.get("/state")
async def state():
    return env.state()
