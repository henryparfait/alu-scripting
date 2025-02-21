#!/usr/bin/python3
"""
Module to query Reddit API and print titles of top 10 hot posts for a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of first 10 hot posts for a subreddit
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    # Reddit API credentials (replace with your own)
    client_id = 'J9j8ihhX78yvCibH3TgVrQ'
    client_secret = 'r_mmX23-2uR6akAivhqxDkP9wv1gRg'
    user_agent = 'python:reddit_top_ten:v1.0 (by /u/Necessary-Floor-9038)'

    # Set up headers with custom User-Agent
    headers = {
        'User-Agent': user_agent
    }

    # URL for subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        # Make GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if request was successful and not redirected
        if response.status_code == 200:
            data = response.json()
            
            # Check if 'data' key exists and has 'children'
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                if not posts:  # Empty subreddit or no posts
                    print(None)
                    return
                
                # Print titles of first 10 posts
                for post in posts[:10]:
                    title = post['data']['title']
                    print(title)
            else:
                print(None)
        else:
            # Invalid subreddit or other error
            print(None)
            
    except requests.RequestException:
        print(None)


if __name__ == '__main__':
    # Example usage
    top_ten("python")
