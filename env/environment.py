from env.models import Observation, Action, Task
class StudentEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tasks = [
    Task(title="Math Homework", completed=False, deadline=3, reward_value=10),
    Task(title="Science Lab Report", completed=False, deadline=4, reward_value=15),
    Task(title="History Reading", completed=False, deadline=2, reward_value=8),
    Task(title="Coding Project", completed=False, deadline=5, reward_value=20)
]
        self.time_left = 5
        self.stress = 0.5
        return self._get_obs()    
    
    def _get_obs(self):
        # Returns the current state packaged in the Observation model
        return Observation(
            tasks=self.tasks,
            time_left=self.time_left,
            stress=self.stress
        )

    def state(self):
        return self._get_obs()

    def step(self, action: Action):
        reward = 0
        
        # --- 1. Stress Management Logic ---
        if action.action_type == "rest":
            self.stress = max(0.0, self.stress - 0.3)
            reward += 5  # Reward for choosing to reduce stress
            
        # --- 2. Task Completion Logic ---
        elif action.action_type == "complete":
            for task in self.tasks:
                if task.title == action.task_title and not task.completed:
                    task.completed = True
                    # Check if the deadline was met
                    if self.time_left >= task.deadline:
                         reward += task.reward_value   # reward based on task
                    else:
                         reward -= task.reward_value // 2  # penalty
                    break

        # --- 3. Update Environment State ---
        self.time_left -= 1
        self.stress += 0.05
        reward -= self.stress * 2
    
        done = self.time_left <= 0 or all(t.completed for t in self.tasks)
        
        return self._get_obs(), reward, done, {}
