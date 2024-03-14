This functions show the manipulation of Reddit API's.
Using python and the Praw library
below is the description of what each module acheaves.

0-subs.py
A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.

1-top_ten.py
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
Prototype: def top_ten(subreddit)
If not a valid subreddit, print None.

2-recurse.py
A recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.
Prototype: def recurse(subreddit, hot_list=[])

100-count.py
A recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords case-insensitive,
delimited by spaces. Javascript should count as javascript
but java should not.
Prototype: def count_words(subreddit, word_list)
