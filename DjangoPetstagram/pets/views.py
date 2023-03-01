from django.shortcuts import render, redirect

from DjangoPetstagram.pets.forms import AddPetForm, EditPetForm, DeletePetForm
from DjangoPetstagram.pets.models import Pet
from DjangoPetstagram.pets.utils import set_photo_count, get_pet_by_slug


def add_pet(request):
    if request.method == 'GET':
        form = AddPetForm()
    else:
        form = AddPetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail_user', pk=1)

    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context)

def delete_pet(request, username, pet_slug):
    the_pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == 'GET':
        form = DeletePetForm(instance=the_pet)
    else:
        form = DeletePetForm(request.POST, instance=the_pet)
        if form.is_valid():
            form.save()
            return redirect('detail_user', pk=1)

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet_slug
    }
    return render(request, 'pets/pet-delete-page.html', context)


def details_pet(request, username, pet_slug):
    #TODO add username when auth
    pet = get_pet_by_slug(slug=pet_slug)
    context = {
        'pet': pet,
        'photos_count': len(set_photo_count(pet)),
        'pet_photos': set_photo_count(pet)
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    the_pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == 'GET':
        form = EditPetForm(instance=the_pet)
    else:
        form = EditPetForm(request.POST, instance=the_pet)
        if form.is_valid():
            form.save()
            return redirect('details_pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'username': username,
        'slug': pet_slug
    }

    return render(request, 'pets/pet-edit-page.html', context)
