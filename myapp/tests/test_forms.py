from django.test import TestCase
from django.test import Client


from myapp.forms import *  # import all forms

class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="user", password="user", first_name="user", email="user@mp.com")

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = Authentic(data={'username':"user", 'password': "user", 'first_name': "user", 'email': "user@mp.com"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data


