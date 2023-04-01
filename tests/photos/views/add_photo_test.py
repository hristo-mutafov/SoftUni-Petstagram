from django.core.files.temp import NamedTemporaryFile
from django.test import TestCase
from django.urls import reverse

from DjangoPetstagram.photos.models import Photo
from tests import signup_user, VALID_USER_DATA


class TestAddPhotoView(TestCase):
    ENDPOINT = 'add_photo'

    def test_add_photo__expect_to_set_user(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        request_data = {
            'photo': '', #TODO
            'description': '',
            'location': 'Test',
        }

        self.client.post(reverse(self.ENDPOINT), data=request_data)
        photo = Photo.objects.all()
        self.assertEqual(user, photo.user)
