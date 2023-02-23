from DjangoPetstagram.pets.models import Pet


def get_pet_by_name(name):
    return Pet.objects.get(name=name)


def set_photo_count(pet):
    return pet.photo_set.all()