from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Log

class LogTests(TestCase):

    @classmethod
    def setUp(cls):
        testuser = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser.save()

        test_log = Log.objects.create(
            name = testuser,
            title = 'Today is Tuesday',
            body = 'and tommorow is Wednesday.'
        )
        test_log.save()

    def test_log_content_happy(self):
        log = Log.objects.get(id=1)
        actual_name= str(log.name)
        actual_title = str(log.title)
        actual_body = str(log.body)
        self.assertEqual(actual_name, 'testuser')
        self.assertEqual(actual_title, 'Today is Tuesday')
        self.assertEqual(actual_body, 'and tommorow is Wednesday.')

    def test_log_content_unhappy(self):
        log = Log.objects.get(id=1)
        actual_name= str(log.name)
        actual_title = str(log.title)
        actual_body = str(log.body)
        self.assertEqual(actual_name, 'testuser')
        self.assertEqual(actual_title, 'Today is Tuesday')
        self.assertIsNot(actual_body, 'and tommorow is Monday.')
