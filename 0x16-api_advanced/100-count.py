#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom_agent"}
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    after = data.get('after')
    posts = data.get('children', [])

    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))

    if after:
        count_words(subreddit, word_list, hot_list, after)
    else:
        word_count = {}
        for word in word_list:
            word_count[word.lower()] = 0

        for title in hot_list:
            for word in word_list:
                word_count[word.lower()] += title.lower().split().count(word.lower())

        sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")

