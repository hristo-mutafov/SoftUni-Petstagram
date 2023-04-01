from django.test import TestCase
from django.urls import reverse

from DjangoPetstagram.pets.models import Pet
from DjangoPetstagram.photos.models import Photo
from tests import signup_user, VALID_USER_DATA
from tests.utils import pet_request_body, create_photos


class TestDetailPetView(TestCase):
    ENDPOINT = 'details_pet'

    def test_detail_pet__is_owner_functionality(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        self.client.post(reverse('add_pet'), data=pet_request_body)
        pet = Pet.objects.get()
        response = self.client.get(reverse('details_pet', kwargs={'username': user.username, 'slug': pet.slug}))
        self.assertTrue(response.context['is_owner'])

    def test_details_pet_photo_count__expect_correct_count(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        self.client.post(reverse('add_pet'), data=pet_request_body)
        pet = Pet.objects.get()
        create_photos(user, 1)
        photo = Photo.objects.get()
        photo.tagged_pets.set((pet, ))
        create_photos(user, 2)
        response = self.client.get(reverse(self.ENDPOINT, kwargs={'username': user.username, 'slug': pet.slug}))
        self.assertEqual(1, response.context['photo_count'])

    def test_details_pet__expect_to_show_all_related_photos(self):
        response_photos = []

        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        self.client.post(reverse('add_pet'), data=pet_request_body)
        pet = Pet.objects.get()
        create_photos(user, 3)
        for i in range(3):
            photo = Photo.objects.all()[i]
            photo.tagged_pets.set((pet,))
            response_photos.append(photo)
        create_photos(user, 2)

        response = self.client.get(reverse(self.ENDPOINT, kwargs={'username': user.username, 'slug': pet.slug}))
        self.assertEqual(response_photos, list(response.context['photos']))
