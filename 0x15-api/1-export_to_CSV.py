#!/usr/bin/python3
"""
Script for fetching data from API for given employee ID,
information about his/ TODO list progress.
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    """
    fetches the user data and the TODO list for the given user ID.
    Store the user ID and surname with the tasks and their status
    Save all of that information on a CSV file
    """

    users_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"

    # Fetch user info
    tasks_response = requests.get(tasks_url)
    users_response = requests.get(users_url)
    # make Json  objects out of responses
    tasks = tasks_response.json()
    users = users_response.json()
    # name the fields for the CSV
    fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    # create the CSV file...
    with open(f"{argv[1]}.csv", 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fields)

        # write the rows
        for task in tasks:
            csv_writer.writerow({
                "USER_ID": '"' + str(users['id']) + '"',
                "USERNAME": '"' + str(users['username']) + '"',
                "TASK_COMPLETED_STATUS": '"' + str(task['completed']) + '"',
                "TASK_TITLE": '"' + str(task['title']) + '"'
            })
