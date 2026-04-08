from fastapi import FastAPI
from env.environment import StudentEnv
from env.models import Action
import uvicorn

app = FastAPI()
env = StudentEnv()

@app.post("/reset")
async def reset():
    return env.reset()

@app.post("/step")
async def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

@app.get("/state")
async def state():
    return env.state()

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# ADD THIS PART AT THE VERY END
if __name__ == "__main__":
    main()
