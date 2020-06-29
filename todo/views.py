"""URLs for our application."""

from flask import redirect, render_template, request
from todo import app

# TODO: Import other functions from the API file
from todo.api import get_tasks, create_task, delete_task, finish_task


@app.route("/")
def tasks_list():
    """ list all the tasks """
    tasks = get_tasks()
    # Render the HTML page located in "templates/application.html"
    # Passing tasks as a variable, so it can be used in the template
    return render_template("application.html", tasks=tasks)


@app.route("/task", methods=["POST"])
def task_create():
    """ Creates a new task using the body paramenter """
    body = request.form["body"]
    create_task(body)
    # Redirect user to the main page, so the new task will be displayed
    return redirect("/")


@app.route("/delete/<int:task_id>")
def task_delete(task_id):
    """Delete task based on task_id"""
    delete_task(task_id)

    # Redirect user back to the main page, so the list of tasks will be updated
    return redirect("/")


@app.route("/done/<int:task_id>")
def task_done(task_id):
    """Mark task as done using task_id"""
    finish_task(task_id)

    return redirect("/")
