from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


UserModel = get_user_model()

class TestRegisterView(TestCase):

    VALID_USER_DATA = {
                'username': 'Test',
                'email': 'test@example.com',
                'password1': 'SomeTestPassword25#!',
                'password2': 'SomeTestPassword25#!'
            }

    def test_register_view__expect_to_login_the_user(self):
        self.client.post(
            reverse('register_user'),
            data=self.VALID_USER_DATA
        )
        cur_user = UserModel.objects.get()
        self.assertTrue(cur_user.is_authenticated)

