"""
tests to create/delete/finish a task

"""

import pytest
from todo.api import get_tasks, create_task, delete_task, finish_task


@pytest.mark.parametrize("task_body", ["buy milk", 2])
def test_list_tasks(task_body):
    n = len(get_tasks())
    task = create_task(task_body)
    # Make sure we have 1 more task now
    assert len(get_tasks()) == n + 1
    assert not task.done
    finish_task(task.id)
    assert task.done
    delete_task(task.id)
    assert len(get_tasks()) == n
