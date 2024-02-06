#!/usr/bin/python3
"""
Script that, using thisST API, for given employee ID,
information about his/ TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    """
    fetches the user data and the TODO list for the given user ID.
    Calculates the number of completed tasks and prints the employee's
    name and the number of completed tasks.
    Prints the title of each completed task.
    """

    users_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"

    response1 = requests.get(tasks_url)
    response2 = requests.get(users_url)

    tasks = response1.json()
    users = response2.json()

    completed_tasks = [task for task in tasks if task['completed']]

    comp = len(completed_tasks)
    out_of = len(tasks)

    print(f"Employee {users['name']} is done with tasks({comp}/{out_of}):",
          end="\n\t ")
    for task in completed_tasks:
        if task['completed'] is True:
            print(task['title'], end="\n\t ")
