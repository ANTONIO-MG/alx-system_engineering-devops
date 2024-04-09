#!/usr/bin/python3
""" a script that queries the Reddit API and returns
the number of subscribers  for a given subreddit """

import requests
from sys import argv


def get_subreddit_subscribers(subreddit_name):
    """ a function that queries the Reddit API and returns
    the number of subscribers  for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit_name}/about.json"

    try:
        response = requests.get(url)
        data = response.json()

        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0

    except Exception as e:
        print("something went wrong:", e)
        return 0

