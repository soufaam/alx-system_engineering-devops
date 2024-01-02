#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
import sys


def exportdata(id_):
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
    with open(f"{id_}.csv", "w") as csv_file:
        csvwriter = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for item in response_todo_json:
            if item.get("userId", None) == id_:
                task_completed_status = item.get("completed", None)
                task_title = item.get("title", None)
                csvwriter.writerow([f"{id_}", name, task_completed_status,
                                    task_title])


if __name__ == "__main__":
    """the entry file"""
    id_ = int(sys.argv[1])
    exportdata(id_=id_)
