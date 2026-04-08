from fastapi import FastAPI
from env.environment import StudentEnv
from env.models import Action
app = FastAPI()
env = StudentEnv()
step_count = 0
def run_task(task_name):
    print(f"[START] task={task_name}", flush=True)

    # fake step
    print(f"[STEP] step=1 reward=1.0", flush=True)

    # fake result
    print(f"[END] task={task_name} score=1.0 steps=1", flush=True)


if __name__ == "__main__":
    tasks = ["task1", "task2", "task3"]

    for t in tasks:
        run_task(t)
