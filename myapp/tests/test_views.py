from django.test import TestCase

class TestCalls(TestCase):
    def test_call_view_deny_anonymous(self):
        response = self.client.get('/url/to/view', follow=True)
        self.assertRedirects(response, '/index/')
        response = self.client.post('/url/to/view', follow=True)
        self.assertRedirects(response, '/index/')

    def test_call_view_load(self):
        self.client.login(username='user', password='user')  # defined in fixture or with factory in setUp()
        response = self.client.get('/url/to/view')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'security.html')


        # etc. ...
