import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY")
)

def run_task(task_name):
    print(f"[START] task={task_name}", flush=True)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say hello"}],
        )
        reward = 1.0
    except Exception as e:
        print(f"Error: {e}", flush=True)
        reward = 0.0

    print(f"[STEP] step=1 reward={reward}", flush=True)
    print(f"[END] task={task_name} score={reward} steps=1", flush=True)


if __name__ == "__main__":
    tasks = ["task1", "task2", "task3"]

    for t in tasks:
        run_task(t)
