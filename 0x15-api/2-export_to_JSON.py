#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys


def exportdata_json(id_):
    """Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress."""
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(id_)
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(url=url_user)
    response_user_json = response_user.json()
    name = response_user_json.get("username", None)
    response_todo = requests.get(url=url_todo)
    response_todo_json = response_todo.json()
    dict_user = {}
    list_tasks = []
    with open(f"{id_}.json", "w") as json_file:
        for item in response_todo_json:
            dict_task = {}
            if item.get("userId", None) == id_:
                dict_task['task'] = item.get("title", None)
                dict_task['completed'] = item.get("completed", None)
                dict_task['username'] = name
                list_tasks.append(dict_task)
        dict_user[f'{id_}'] = list_tasks
        json.dump(dict_user, json_file)


if __name__ == "__main__":
    """the entry file"""
    id_ = int(sys.argv[1])
    exportdata_json(id_=id_)
