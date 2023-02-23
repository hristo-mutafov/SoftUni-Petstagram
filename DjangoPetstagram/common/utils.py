from DjangoPetstagram.photos.models import Photo


def get_likes(photo_obj):
    photo_obj.like_count = photo_obj.photolike_set.count()
    return photo_obj
def check_if_liked(photo_obj):
    photo_obj.is_liked = photo_obj.like_count > 0
    return photo_obj

def get_photo_by_id(photo_id):
    return Photo.objects.get(id=photo_id)