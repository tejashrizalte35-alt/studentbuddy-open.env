import os
from env.environment import StudentEnv
from env.models import Action
from env.grader import grade
                               
task_name = os.getenv("TASK_NAME", "student_study_buddy")
print(f"[START] task={task_name}", flush=True)

env = StudentEnv()
obs = env.reset()

done = False
step_num = 0
total_reward = 0

while not done:
    # Increment step
    step_num += 1
    
    task = next((t for t in obs.tasks if not t.completed), None)
    
    if task:
        action = Action(action_type="complete", task_title=task.title)
    else:
        action = Action(action_type="rest")

    # Perform action
    obs, reward, done, _ = env.step(action)
    total_reward += reward
    
    print(f"[STEP] step={step_num} reward={reward}", flush=True)

# Calculate final results
score = grade(env)
total_steps = step_num

print(f"[END] task={task_name} score={score} steps={total_steps}", flush=True)

print("Final Score:", score)
