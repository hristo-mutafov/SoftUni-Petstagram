from DjangoPetstagram.pets.models import Pet


def get_pet_by_slug(slug):
    return Pet.objects.get(slug=slug)


def set_photo_count(pet):
    return pet.photo_set.all()