#!/usr/bin/python3
"""
Module to query the Reddit API and print titles of the first 10 hot posts
for a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Prints titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    url = "https://www.reddit.com/r/Music/".format(subreddit)
    headers = {'User-Agent': 'linux:0:1.0 (by /u/Necessary-Floor-9038)'}
    params = {"limit": 10}

    try:
        # Make GET request without following redirects
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        # Check status code for success or invalid subreddit
        if response.status_code == 200:
            data = response.json()
            # Verify 'data' and 'children' exist in response
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                if not posts:  # No posts in subreddit
                    print(None)
                    return
                # Print titles of first 10 posts
                for post in posts[:10]:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            # Invalid subreddit or other HTTP error (e.g., 404, 302)
            print(None)

    except requests.RequestException:
        # Handle network errors or invalid requests
        print(None)


if __name__ == '__main__':
    # Example usage
    top_ten("python")
