#!/usr/bin/python3
"""  a script that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit. """

import praw
from sys import argv

def top_ten(subreddit):
    """  a function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit. """
    
    reddit = praw.Reddit(client_id='Sd8ya0rJ_esCfWq2aKIxEg',
                         client_secret='favSH52deAviKnTIhzck0JdUUNnu8A',
                         user_agent='testing 123')
    
    try:
        # check if the subreddit exits and return the number of subscribers
        subreddit_obj = reddit.subreddit(subreddit)
        print(subreddit)
        
        for submission in subreddit_obj.hot(limit=10):
            print(submission.title)
    except:
        # else if it does not exist return 0
        print("None")


if  __name__ == "__main__":
    """
    if module is executed  as a script, then print out the number of
    """
    top_ten(argv[1])