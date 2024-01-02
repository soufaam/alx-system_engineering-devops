#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys


def exportdata_json():
    """Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress."""
    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    response_users = requests.get(url=url_user)
    response_users_json = response_users.json()
    response_todo = requests.get(url=url_todo)
    response_todo_json = response_todo.json()
    dict_users = {}
    with open(f"todo_all_employees.json", "w") as json_file:
        for user in response_users_json:
            list_tasks = []
            for item in response_todo_json:
                if item.get("userId", None) == user.get("id"):
                    dict_task = {}
                    dict_task['task'] = item.get("title", None)
                    dict_task['completed'] = item.get("completed", None)
                    dict_task['username'] = user.get("username", None)
                    list_tasks.append(dict_task)
                    dict_users[user.get("id")] = list_tasks
        json.dump(dict_users, json_file)


if __name__ == "__main__":
    """the entry file"""
    exportdata_json()
