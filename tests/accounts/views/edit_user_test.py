from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestEditUser(TestCase):
    MAIN_ENDPOINT = 'edit_user'

    VALID_USER_DATA = {
        'username': 'Test',
        'email': 'test@example.com',
        'password': 'SomeTestPassword25#!'
    }

    def signup_user(self):
        user = UserModel.objects.create(
            **self.VALID_USER_DATA
        )
        user.set_password(self.VALID_USER_DATA['password'])
        user.save()
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_edit_user__when_new_email_added__expect_changes_in_main_user_model(self):
        user = self.signup_user()
        new_email = 'new_email@gmail.com'

        valid_data = {
            'first_name': '',
            'last_name': '',
            'gender': '',
            'profile_picture': '',
            'email': new_email,
        }

        self.client.post(reverse(self.MAIN_ENDPOINT, kwargs={'pk': user.pk}), data=valid_data)
        self.assertEqual(new_email, UserModel.objects.get().email)

