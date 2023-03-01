from django.shortcuts import render, redirect

from DjangoPetstagram.common.forms import CommentForm
from DjangoPetstagram.common.utils import get_likes
from DjangoPetstagram.photos.forms import AddPhotoForm, EditPhotoForm, DeletePhotoForm
from DjangoPetstagram.photos.models import Photo
from DjangoPetstagram.photos.utils import get_photo_by_pk


def add_photo(request):
    if request.method == 'GET':
        form = AddPhotoForm()
    else:
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return redirect('details_photo', pk=photo.pk)

    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)

def details_photo(request, pk):
    photo = get_likes(get_photo_by_pk(pk))
    form = CommentForm()
    context = {
        'photo':  photo,
        'comments': photo.photocomment_set.all(),
        'pk': pk,
        'form': form
    }
    return render(request, 'photos/photo-details-page.html', context)

def edit_photo(request, pk):
    pet = Photo.objects.filter(id=pk).get()
    if request.method == 'GET':
        form = EditPhotoForm(instance=pet)
    else:
        form = EditPhotoForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            photo = form.save()
            return redirect('details_photo', pk=photo.pk)
    context = {
        'form': form,
        'pk': pk
    }
    return render(request, 'photos/photo-edit-page.html', context)

def delete_photo(request, pk):
    pet = Photo.objects.filter(id=pk).get()
    if request.method == 'GET':
        form = DeletePhotoForm(instance=pet)
    else:
        form = DeletePhotoForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'pk': pk
    }
    return render(request, 'photos/photo-delete-page.html', context)