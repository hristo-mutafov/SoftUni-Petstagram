from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from DjangoPetstagram.accounts.models import UserProfile

UserModel = get_user_model()

class TestUserModel(TestCase):
    VALID_USER_DATA = {
        'username': 'Test',
        'email': 'test@example.com',
        'password1': 'SomeTestPassword25#!',
        'password2': 'SomeTestPassword25#!'
    }

    def test_user_model__when_register__expect_to_create_user_profile_instance(self):
        self.client.post(
            reverse('register_user'),
            data=self.VALID_USER_DATA
        )
        current_user = UserModel.objects.get()
        profile = UserProfile.objects.get().user
        self.assertEqual(current_user, profile)
