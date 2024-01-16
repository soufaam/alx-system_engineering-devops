#!/usr/bin/python3
"""A script contains number_of_subscribers function
"""
import requests
from pprint import pprint


def top_ten(subreddit):
    """function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for a given subreddit.
    Args:
        subreddit (String): a given subscribers in Reddit
    Returns: int value
    """
    headers = {'User-Agent': "Mozilla/115.5.0"}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url=url, headers=headers)
    if response.status_code != 404:
        data_json = response.json()
        data_parsed = data_json['data']
        data_list = data_parsed['children']
        if data_list == []:
            print(None)
            return
        for item in data_list:
            print(item['data']['title'])
    else:
        print(None)
