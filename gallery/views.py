from django.shortcuts import render

def photo_gallery(request):
    return render(request, 'gallery/photo_gallery.html', {})
