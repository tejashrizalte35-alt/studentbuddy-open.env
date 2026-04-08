from env.models import Observation, Action, Task

class StudentEnv:
    def __init__(self):
        self.reset()
self.tasks = [
    Task(title="Math Homework", completed=False),
    Task(title="Science Lab Report", completed=False),
    Task(title="History Reading", completed=False),
    Task(title="Coding Project", completed=False) # Adding a 4th for safety!
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
                        reward += 10
                    else:
                        reward -= 5  # Penalty for finishing after the deadline
                    break

        # --- 3. Update Environment State ---
        self.time_left -= 1
        # Stress naturally increases slightly over time
        self.stress += 0.05
        
        # Check if the session is finished
        # Done if time is up OR all tasks are completed
        done = self.time_left <= 0 or all(t.completed for t in self.tasks)
        
        return self._get_obs(), reward, done, {}
