#!/usr/bin/python3
"""
Script that, using thisST API, for given employee ID,
information about his/ TODO list progress.
"""
import csv
import json
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

    fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open("USER_ID.csv", 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fields)

        # write the header
        csv_writer.writeheader()

        # write the rows
        for task in tasks:
            csv_writer.writerow({
                "USER_ID": users['id'],
                "USERNAME": users['name'],
                "TASK_COMPLETED_STATUS": task['completed'],
                "TASK_TITLE": task['title']
            })
