from env.environment import StudentEnv
from env.models import Action
from env.grader import grade  # Import your grader to see your final score

env = StudentEnv()
obs = env.reset()
done = False
total_reward = 0

print("--- Starting Study Session ---")
# Run the loop until the environment says 'done'
while not done:
    target_task = next((t for t in obs.tasks if not t.completed), None)
    #action = Action(action_type="complete", task_title="Math") 
    if target_task:
        # If there's work to do, complete it
        action = Action(action_type="complete", task_title=target_task.title)
        print(f"Action: Completing {target_task.title}")
    else:
        # If all tasks are finished, take a rest to lower stress
        action = Action(action_type="rest", task_title="")
        print("Action: All tasks done! Taking a rest.")
    obs, reward, done, _ = env.step(action)
    total_reward += reward
    print(f"Action taken. Current Reward: {reward} | Total: {total_reward}| Stress: {obs.stress:.2f}")

# After the loop finishes, evaluate the performance
final_score = grade(env)
print("--- Session Finished ---")
print(f"Final Grader Score: {final_score}")