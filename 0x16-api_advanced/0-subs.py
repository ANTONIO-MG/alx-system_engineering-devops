#!/usr/bin/python3
""" a script that queries the Reddit API and returns
the number of subscribers  for a given subreddit """

import praw
from sys import argv

def get_subreddit_subscribers(subreddit_name):
    """ a function that queries the Reddit API and returns
    the number of subscribers  for a given subreddit """
    
    reddit = praw.Reddit(client_id='Sd8ya0rJ_esCfWq2aKIxEg',
                         client_secret='favSH52deAviKnTIhzck0JdUUNnu8A',
                         user_agent='testing 123')
    
    try:
        # check if the subreddit exits and return the number of subscribers
        subreddit = reddit.subreddit(subreddit_name) 
        subscribers_count = subreddit.subscribers
        return subscribers_count
    except:
        # else if it does not exist return 0
        return 0


if  __name__ == "__main__":
    """
    if module is executed  as a script, then print out the number of
    """
    get_subreddit_subscribers(argv[1])