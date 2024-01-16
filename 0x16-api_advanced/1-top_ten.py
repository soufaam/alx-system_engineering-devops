#!/usr/bin/python3
"""A script contains number_of_subscribers function
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts
    listed for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url=url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        print(None)
        return
    subs = resp.json().get("data")
    for post in subs.get("children"):
        post_details = post.get("data")
        print(post_details.get("title"))
