from fastapi import FastAPI
from env.environment import StudentEnv
from env.models import Action
app = FastAPI()
env = StudentEnv()
step_count = 0

@app.post("/openenv/reset")
def reset():
    global step_count
    step_count = 0

    print("[START] task=StudentEnv", flush=True)
    return env.reset()

    return env.reset()

@app.get("/openenv/state")
def state():
    return env.state()

@app.post("/openenv/step")
def step(action: Action):
    global step_count
    step_count += 1

    obs, reward, done, info = env.step(action)
    print("[START] task=StudentEnv", flush=True)
    
    print(f"[STEP] step={step_count} reward={reward}", flush=True)
    if done:
    print(f"[END] task=StudentEnv score={reward} steps={step_count}", flush=True)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }
