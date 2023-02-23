import http
from django.http import HttpResponse
from django.shortcuts import render, redirect

from DjangoPetstagram.common.models import PhotoLike, PhotoComment
from DjangoPetstagram.common.utils import get_likes, check_if_liked, get_photo_by_id
from DjangoPetstagram.photos.models import Photo


def index(request):
    photos = [get_likes(photo) for photo in Photo.objects.all()]
    photos = [check_if_liked(photo) for photo in photos]
    context = {
        'photos': photos
    }
    return render(request, 'common/home-page.html', context)

def like(request, photo_id):
    photo = get_photo_by_id(photo_id)
    get_likes(photo)
    if photo.like_count:
        [obj.delete() for obj in photo.photolike_set.all()]
    else:
        PhotoLike.objects.create(
            photo=photo
        )
    return redirect('index')
