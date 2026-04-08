def grade_task(task):
    if task.completed:
        return 0.95
    else:
        return 0.05

def grade(env):
    if len(env.tasks) < 3:
        return 0.1 

    total_score = sum(grade_task(t) for t in env.tasks)
    final_score = total_score / len(env.tasks)
    
    return final_score
