def grade(env):
    completed = sum(1 for t in env.tasks if t.completed)

    if completed == 3 and env.stress < 0:
        return 1.0
    elif completed >= 2:
        return 0.6
    elif completed == 1:
        return 0.3
    else:
        return 0.0