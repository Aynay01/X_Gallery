from django.shortcuts import render
from .twitter_utils import fetch_images_from_twitter

def photo_gallery(request):
    hashtag = '#carnival'
    image_urls = fetch_images_from_twitter(hashtag)
    return render(request, 'gallery/photo_gallery.html', {'image_urls': image_urls})