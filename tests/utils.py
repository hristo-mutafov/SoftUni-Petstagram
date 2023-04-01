from django.contrib.auth import get_user_model

from DjangoPetstagram.common.models import PhotoLike
from DjangoPetstagram.photos.models import Photo

UserModel = get_user_model()

VALID_USER_DATA = {
        'username': 'Test',
        'email': 'test@example.com',
        'password': 'SomeTestPassword25#!'
    }

pet_request_body = {
            'name': 'Test',
            'date_of_birth': '2023-03-30',
            'personal_photo': 'http://www.example.com/photos',
        }
def signup_user():
    user = UserModel.objects.create(
        **VALID_USER_DATA
    )
    user.set_password(VALID_USER_DATA['password'])
    user.save()
    return user

def create_photos(user, count, like=False):

    for i in range(count):
        photo = Photo.objects.create(
            location=f'Test{i}',
            user=user,
        )
        if like:
            add_like(photo, user)


def add_like(photo, user):
    PhotoLike.objects.create(
        photo=photo,
        user=user
    )

