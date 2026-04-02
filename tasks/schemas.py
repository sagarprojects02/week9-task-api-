def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "status": task.status
    }
