from fastapi import FastAPI
from env.environment import StudentEnv
from env.models import Action
app = FastAPI()
env = StudentEnv()
step_count = 0
@app.post("/openenv/step")
def step(action: Action):
    global step_count
    step_count += 1

    obs, reward, done, info = env.step(action)

    # STEP log
    print(f"[STEP] step={step_count} reward={reward}", flush=True)

    # END log
    if done:
        print(f"[END] task=StudentEnv score={reward} steps={step_count}", flush=True)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }
