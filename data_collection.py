import tweepy
import re

def remove_urls_and_hashtags(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    text = url_pattern.sub('', text)

    hashtag_pattern = re.compile(r'#\w+\s?')
    text = hashtag_pattern.sub('', text)

    attherate_pattern = re.compile(r'@\w+\s?')
    text = attherate_pattern.sub('', text)

    text = text.translate(str.maketrans('', '', '"*:?,.!-\''))
    text = text.replace('`', '')
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text



def get_data(query, BEARER_TOKEN):
    data = []
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=5000):
        text = remove_urls_and_hashtags(tweet.text)
        data.append(text)

    with open('data.txt', 'w', encoding='utf-8') as f:
        for d in data:
            f.write("%s\n" % d)
    return data
