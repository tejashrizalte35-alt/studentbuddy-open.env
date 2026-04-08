def grade(env):
    completed_tasks = [t for t in env.tasks if t.completed]
    # Ensure this logic accounts for at least 3 tasks
    if len(env.tasks) < 3:
        return 0 
    score = len(completed_tasks) / len(env.tasks)
    return score
