#!/usr/bin/python3
"""

Uses reddit API to get 10 hot posts

"""

import requests


def top_ten(subreddit):
    """Get 10 hot posts"""
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers={'User-Agent': 'request'},
        response = requests.get(url, headers=headers, allow_redirects=false)

    

    if response.status_code != 200:
        print(None)
        return
    

    data = response.json().get("data").get("children")
    top_10_posts = "\n".join(post.get("data").get("title") for post in data)
    print(top_10_posts)
