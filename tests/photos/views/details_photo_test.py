from django.test import TestCase
from django.urls import reverse

from DjangoPetstagram.photos.models import Photo
from tests import signup_user, create_photos, VALID_USER_DATA


class TestDetailsPhotoView(TestCase):
    ENDPOINT = 'details_photo'

    def test_details_photo__expect_is_owner_to_be_true(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        create_photos(user, 1)
        photo = Photo.objects.get()
        response = self.client.get(reverse(self.ENDPOINT, kwargs={'pk': photo.pk}))
        self.assertTrue(response.context['is_owner'])

    def test_details_photo__expect_is_owner_to_be_false(self):
        user = signup_user()
        create_photos(user, 1)
        photo = Photo.objects.get()
        response = self.client.get(reverse(self.ENDPOINT, kwargs={'pk': photo.pk}))
        self.assertTrue(not response.context['is_owner'])


    def test_details_photo__expect_right_likes_count(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        create_photos(user, 1, like=True)
        photo = Photo.objects.get()
        response = self.client.get(reverse(self.ENDPOINT, kwargs={'pk': photo.pk}))
        self.assertEqual(1, response.context['photo'].like_count)

