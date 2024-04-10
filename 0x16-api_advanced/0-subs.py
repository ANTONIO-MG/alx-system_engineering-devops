#!/usr/bin/python3
""" a script that queries the Reddit API and returns
the number of subscribers  for a given subreddit """

import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns
    the number of subscribers  for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    user_agent = {'User-Agent': 'Python/requests'}

    response = requests.get(url, headers=user_agent,
                            allow_redirects=False)

    if response.status_code in [302, 404]:
        return 0

    return response.json().get('data').get('subscribers')


if __name__ == "__main__":
    """ if module is executed  as a script,
    then print out the number of
    """

    number_of_subscribers()
