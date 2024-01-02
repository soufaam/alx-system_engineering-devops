#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


if __name__ == "__main__":
    id_ = int(sys.argv[1])
    """Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress."""
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(id_)
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(url=url_user)
    response_user_json = response_user.json()
    name = response_user_json.get("name", None)
    response_todo = requests.get(url=url_todo)
    response_todo_json = response_todo.json()
    total_tasks = 0
    completed_tasks_number = 0
    completed_tasks = []
    for item in response_todo_json:
        if item.get("userId", None) == id_:
            total_tasks += 1
            if item.get("completed"):
                completed_tasks_number += 1
                completed_tasks.append(item.get("title", None))
    print("Employee {} is done with tasks\
({}/{}):".format(name, completed_tasks_number, total_tasks))
    for com in completed_tasks:
        print("\t {}".format(com))
