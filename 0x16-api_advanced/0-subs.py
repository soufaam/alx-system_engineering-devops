#!/usr/bin/python3
"""A script contains number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit=None):
    """A afunction that queries the Reddit
API and returns the number of subscribers
    Args:
        subreddit (String): a given subscribers in Reddit
    Returns: int value
    """
    headers = {'User-Agent': "Mozilla/5.0"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        data_json = response.json()
        data_parsed = data_json['data']
        return data_parsed.get('subscribers', 0)
    else:
        return 0
