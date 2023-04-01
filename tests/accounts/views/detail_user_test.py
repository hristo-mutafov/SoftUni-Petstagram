from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tests.utils import create_photos, signup_user, VALID_USER_DATA

UserModel = get_user_model()

class TestDetailUserView(TestCase):
    DETAIL_ENDPOINT = 'detail_user'

    def test_detail_user__when_the_user_is_the_owner__expect_is_owner_to_be_true(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)

        response = self.client.get(
            reverse('detail_user', kwargs={'pk': user.pk})
        )

        self.assertTrue(response.context['is_owner'])

    def test_detail_user__when_user_have_no_pets__expect_zero_pets_count(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)

        response = self.client.get(reverse(self.DETAIL_ENDPOINT, kwargs={'pk': user.pk}))
        self.assertEqual(0, response.context['pets'].count())

    def test_detail_user__when_pets_expect_correct_pets_count(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        for i in range(3):
            self.client.post(reverse('add_pet'), data={
                'name': f'Test{i}',
                'personal_photo': f'https://test{i}.com/wp-content/uploads/2022/07/test.jpg',
                'user': user
            })

        response = self.client.get(reverse(self.DETAIL_ENDPOINT, kwargs={'pk': user.pk}))
        self.assertEqual(3, response.context['pets'].count())

    def test_detail_user__when_no_photos__expect_zero_photos_count(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)

        response = self.client.get(reverse(self.DETAIL_ENDPOINT, kwargs={'pk': user.pk}))
        self.assertEqual(0, response.context['photos'].count())

    def test_detail_user__when_photos__expect_correct_photos_count(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        create_photos(user, 3)
        response = self.client.get(reverse(self.DETAIL_ENDPOINT, kwargs={'pk': user.pk}))
        self.assertEqual(3, response.context['photos'].count())

    def test_detail_user__when_not_likes__expect_zero_likes_count(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        create_photos(user, 3)
        response = self.client.get(reverse(self.DETAIL_ENDPOINT, kwargs={'pk': user.pk}))
        self.assertEqual(0, response.context['likes'])

    def test_details_user__when_have_likes_from_different_photos__expect_to_sum_the_likes(self):
        user = signup_user()
        self.client.login(**VALID_USER_DATA)
        create_photos(user, 3, like=True)
        response = self.client.get(reverse(self.DETAIL_ENDPOINT, kwargs={'pk': user.pk}))
        self.assertEqual(3, response.context['likes'])


