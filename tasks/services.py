from tasks.models import Task


class TaskService:
    @staticmethod
    def mark_as_completed(task: Task):
        task.completed = True
        task.save()
        return task
