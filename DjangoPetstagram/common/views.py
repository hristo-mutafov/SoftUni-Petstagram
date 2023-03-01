import http
from django.http import HttpResponse
from django.shortcuts import render, redirect

from DjangoPetstagram.common.forms import CommentForm, SearchByPetForm
from DjangoPetstagram.common.models import PhotoLike, PhotoComment
from DjangoPetstagram.common.utils import get_likes, check_if_liked, get_photo_by_id
from DjangoPetstagram.photos.models import Photo


def index(request):
    photos = None
    search_form = SearchByPetForm(request.GET)
    search_form.is_valid()
    if search_form.cleaned_data['pet_name']:
        filter_by = search_form.cleaned_data['pet_name']
        photos = Photo.objects.filter(tagged_pets__name__icontains=filter_by).all()
    else:
        photos = Photo.objects.all()

    photos = [get_likes(photo) for photo in photos]
    photos = [check_if_liked(photo) for photo in photos]
    form = CommentForm()
    comments = PhotoComment.objects.first()
    context = {
        'photos': photos,
        'form': form,
        'comment': comments,
        'search_form': search_form
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

def comment(request, pk):
    photo = Photo.objects.filter(id=pk).get()

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()
    return redirect('details_photo', pk=pk)


