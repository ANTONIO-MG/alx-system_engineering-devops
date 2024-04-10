#!/usr/bin/python3
""" A recursive Script that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit """

import requests
from sys import argv


def recurse(subreddit, hot_list=None, after=None):
    """A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit."""

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    user_agent = {'User-Agent': "Python/requests"}

    try:
        params = {'after': after} if after else {}
        response = requests.get(url, headers=user_agent,
                                params=params, allow_redirects=False)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:  # recursively call the function with the 'after'
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None

    except Exception as e:
        print("None:", e)
        return None


if __name__ == "__main__":
    """
    if module is executed  as a script, then print out the number of
    """

    recurse(argv[1])
