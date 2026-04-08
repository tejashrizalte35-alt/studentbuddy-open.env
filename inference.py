import os
from openai import OpenAI
from env.environment import StudentEnv
from env.models import Action
from env.grader import grade
client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"), 
    api_key=os.environ.get("API_KEY")
)

task_name = os.getenv("TASK_NAME", "student_study_buddy")
print(f"[START] task={task_name}", flush=True)

env = StudentEnv()
obs = env.reset()
done = False
step_num = 0

while not done:
    step_num += 1
    unfinished_tasks = [t.title for t in obs.tasks if not t.completed]
    
    if unfinished_tasks:
        response = client.chat.completions.create(
            model="gpt-4o", # Meta/Scaler usually supports gpt-4o or llama-3
            messages=[
                {"role": "system", "content": "You are a helpful study buddy. Pick one task from the list and return ONLY the task name."},
                {"role": "user", "content": f"Remaining tasks: {unfinished_tasks}"}
            ]
        )

        chosen_task_title = response.choices[0].message.content.strip()
    
            action = Action(action_type="complete", task_title=chosen_task_title)
        else:
            action = Action(action_type="complete", task_title=unfinished_tasks[0])
    else:
        action = Action(action_type="rest")

    # Perform the action in OpenEnv
    obs, reward, done, _ = env.step(action)
    print(f"[STEP] step={step_num} reward={reward}", flush=True)

# Final Scoring
score = grade(env)
print(f"[END] task={task_name} score={score} steps={step_num}", flush=True)
