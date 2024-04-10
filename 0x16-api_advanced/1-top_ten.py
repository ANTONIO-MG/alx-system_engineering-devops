#!/usr/bin/python3
"""  a script that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit. """

import requests
from sys import argv


def top_ten(subreddit):
    """  a function that queries the Reddit API and
    prints the titles of the first
    10 hot posts listed for a given subreddit. """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    user_agent = {'User-Agent': "Python/requests"}

    try:
        response = requests.get(url, headers=user_agent,
                                allow_redirects=False)
        titles = response.json()['data']['children']

        if response.status_code != 200:
            return None
        else:
            for title in titles:
                print(title['data']['title'])

    except Exception as e:
        print("None:", e)


if __name__ == "__main__":
    """
    if module is executed  as a script, then print out the number of
    """

    top_ten(argv[1])
