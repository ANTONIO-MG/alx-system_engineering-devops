#!/usr/bin/python3
""" A recursive Script that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit """

import praw
from sys import argv

count = 0

def recurse(subreddit_name, count=0, hot_list=None):
    """A recursive function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit."""
    
    # Initialize hot_list if not provided
    if hot_list is None:
        hot_list = []

    reddit = praw.Reddit(client_id='Sd8ya0rJ_esCfWq2aKIxEg',
                         client_secret='favSH52deAviKnTIhzck0JdUUNnu8A',
                         user_agent='testing 123')
    
    try:
        # Check if the subreddit exists
        subreddit = reddit.subreddit(subreddit_name)
        
        for submission in subreddit.hot():
            count += 1
    except:
        # If the subreddit does not exist, return 0 and an empty list
        print("Subreddit '{}' not found or private.".format(subreddit_name))
        return count
    
    # Recursive call to fetch more titles if needed
    return recurse(subreddit_name, count=count, hot_list=hot_list)


if  __name__ == "__main__":
        """
        if module is executed  as a script, then print out the number of
        """
        print(recurse("programming"))