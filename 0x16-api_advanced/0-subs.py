#!/usr/bin/python3
"""A script contains number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit=None):
    """A afunction that queries the Reddit
API and returns the number of subscribers
    Args:
        subreddit (String): a given subscribers in Reddit
    """
    headers = {'User-Agent': 'Script get subreddit Data /1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        data_json = response.json()
        data_parsed = data_json['data']
        return data_parsed.get('subscribers', 0)
    else:
        return 0
