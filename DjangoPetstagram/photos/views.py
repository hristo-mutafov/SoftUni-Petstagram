from django.shortcuts import render

from DjangoPetstagram.common.utils import get_likes
from DjangoPetstagram.photos.models import Photo
from DjangoPetstagram.photos.utils import get_photo_by_pk


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')

def details_photo(request, pk):
    photo = get_likes(get_photo_by_pk(pk))
    context = {
        'photo':  photo,
        'comments': photo.photocomment_set.all()
    }
    return render(request, 'photos/photo-details-page.html', context)

def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')