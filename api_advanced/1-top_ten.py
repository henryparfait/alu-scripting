#!/usr/bin/python3
"""Function that queries the Reddit API and prints top 10 hot post titles."""
import requests
import sys

def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    If not a valid subreddit, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:0:1.0 (by /u/JuiceExtension6952)'
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    title = post.get('data', {}).get('title')
                    print(title)
            else:
                print(None)
        else:
            print(None)
    except Exception:
        print(None)
