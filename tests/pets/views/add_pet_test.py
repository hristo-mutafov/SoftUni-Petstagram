from django.test import TestCase
from django.urls import reverse

from DjangoPetstagram.pets.models import Pet
from tests import signup_user, VALID_USER_DATA
from tests.utils import pet_request_body


class TestAddPetView(TestCase):
    ENDPOINT = 'add_pet'

    def test_add_pet__expect_to_sign_the_right_user(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        self.client.post(reverse(self.ENDPOINT), data=pet_request_body)
        pet = Pet.objects.get()
        self.assertEqual(user, pet.user)


