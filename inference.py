from fastapi import FastAPI
from env.environment import StudentEnv
from env.models import Action

app = FastAPI()

env = StudentEnv()

@app.post("/openenv/reset")
def reset():
    return env.reset()

@app.get("/openenv/state")
def state():
    return env.state()

@app.post("/openenv/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }
