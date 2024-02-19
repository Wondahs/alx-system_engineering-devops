#!/usr/bin/python3
'''for a given employee ID, returns information about his/her TODO list progress.'''
from sys import argv, exit
import requests

import logging
#logging.basicConfig(level=logging.DEBUG)

if len(argv) < 2:
    exit(-1)

user_id = argv[1]


def get_username(user_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    #print("Making request now...")
    response = requests.get(user_url)
    if response.status_code == 200:
        #print("Request successful. Getting data now")
        data = response.json()
        return data.get('name')

username = get_username(user_id)
print(username)

def get_todos(user_id):
    todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(todo_url)
    if response.status_code == 200:
        data = response.json()
        return data

todos = get_todos(user_id)
print(todos)

def parse(username, todos):
    completed = []
    total_tasks = 0
    for todo in todos:
        total_tasks += 1
        if todo.get('completed') == True:
            completed.append(todo.get('title'))
    completed_tasks = len(completed)
    print(f"Employee {username} is done with tasks({completed_tasks/total_tasks})")
    for task in completed:
        print(f"\t {task}")

