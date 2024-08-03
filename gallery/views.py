
from django.shortcuts import render
from TwitterAPI import TwitterAPI
from django.conf import settings

def fetch_images_from_twitter(hashtag):
    api = TwitterAPI(
        settings.TWITTER_API_KEY,
        settings.TWITTER_API_SECRET_KEY,
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_TOKEN_SECRET
    )

    # Search for tweets with the specified hashtag
    response = api.request('search/tweets', {'q': hashtag, 'count': 100, 'tweet_mode': 'extended'})
    
    if response.status_code == 200:
        tweets = response.json()['statuses']
        image_urls = []
        
        for tweet in tweets:
            media = tweet['entities'].get('media', [])
            for item in media:
                if item['type'] == 'photo':
                    image_urls.append(item['media_url'])
        
        return image_urls
    else:
        return []

def photo_gallery(request):
    hashtag = '#carnival'
    image_urls = fetch_images_from_twitter(hashtag)
    return render(request, 'gallery/photo_gallery.html', {'photos': image_urls})