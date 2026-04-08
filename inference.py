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
        try:
            # Wrap the API call in a try block
            response = client.chat.completions.create(
                model="gpt-4o", 
                messages=[
                    {"role": "system", "content": "You are a helpful study buddy. Pick one task and return ONLY the task name."},
                    {"role": "user", "content": f"Remaining tasks: {unfinished_tasks}"}
                ],
                timeout=30.0 # Add a timeout so it doesn't hang forever
            )
            chosen_task_title = response.choices[0].message.content.strip()
        except Exception as e:
            # If the API fails, print the error and use a fallback
            print(f"API Call failed: {e}")
            chosen_task_title = unfinished_tasks[0] 
        
        # Now define the action using the result (or the fallback)
        if chosen_task_title in unfinished_tasks:
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
