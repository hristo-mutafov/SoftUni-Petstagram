from DjangoPetstagram.photos.models import Photo


def get_photo_by_pk(pk):
    return Photo.objects.get(id=pk)