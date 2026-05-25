"""API functions to interact with TODO tasks."""

from todo.models import Task, db


def get_tasks():
    """returns all tasks"""
    return Task.query.all()


def create_task(body):
    """adds task to the database"""
    task = Task(body=body, done=False)
    db.session.add(task)
    db.session.commit()
    return task


def delete_task(task_id):
    """delete a task from the database"""
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()


def finish_task(task_id):
    """mark task as done"""
    task = Task.query.filter_by(id=task_id).first()
    task.done = True
    db.session.commit()
