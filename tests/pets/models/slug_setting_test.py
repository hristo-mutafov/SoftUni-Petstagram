from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from DjangoPetstagram.pets.models import Pet
from tests import signup_user, VALID_USER_DATA


pet_request_body = {
            'name': 'Test',
            'date_of_birth': '2023-03-30',
            'personal_photo': 'http://www.example.com/photos',
        }


class TestSlugSetting(TestCase):

    def test_slug_setting(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        self.client.post(reverse('add_pet'), data=pet_request_body)
        pet = Pet.objects.get()
        self.assertEqual(slugify(f'{pet.id}-{pet.name}'), pet.slug)
