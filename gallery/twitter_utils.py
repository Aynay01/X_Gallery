import tweepy
from django.conf import settings

def fetch_images_from_twitter(hashtag):
    # Authenticate to Twitter
    auth = tweepy.OAuth1UserHandler(
        settings.TWITTER_API_KEY,
        settings.TWITTER_API_SECRET_KEY,
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)

    # Fetch tweets containing the hashtag
    tweets = api.search_tweets(q=hashtag, count=100, tweet_mode='extended')

    image_urls = []
    for tweet in tweets:
        if 'media' in tweet.entities:
            for media in tweet.entities['media']:
                if media['type'] == 'photo':
                    image_urls.append(media['media_url'])

    return image_urls