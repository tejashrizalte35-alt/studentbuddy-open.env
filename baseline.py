from env.environment import StudentEnv
from env.models import Action
from env.grader import grade

env = StudentEnv()
obs = env.reset()

done = False

while not done:
    # simple logic: complete first unfinished task
    task = next((t for t in obs.tasks if not t.completed), None)

    if task:
        action = Action(action_type="complete", task_title=task.title)
    else:
        action = Action(action_type="rest")

    obs, reward, done, _ = env.step(action)

score = grade(env)
print("Final Score:", score)