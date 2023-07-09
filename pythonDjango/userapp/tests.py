from django.test import TestCase
from django.urls import reverse

from .models import User

class UserListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 users for pagination tests
        number_of_users = 13

        for user_id in range(number_of_users):
            User.objects.create(
                firstName=f'Christian {user_id}',
                lastName=f'Surname {user_id}',
                email=f'christian{user_id}@example.com',
                username=f'christian{user_id}',
                password=f'pass{user_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('list_users'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('list_users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userapp/list_users.html')
