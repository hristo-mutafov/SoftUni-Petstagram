from django.shortcuts import render

from DjangoPetstagram.pets.utils import get_pet_by_name, set_photo_count


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')

def delete_pet(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')


def details_pet(request, username, pet_name):
    pet = get_pet_by_name(pet_name)
    context = {
        'pet': pet,
        'photos_count': len(set_photo_count(pet)),
        'pet_photos': set_photo_count(pet)
    }
    return render(request, 'pets/pet-details-page.html', context)

def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')
