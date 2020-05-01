from django.test import TestCase
from django.urls import reverse,resolve
from bus_reserve.views import index

class TestUrls(TestCase):
    def testurls(self):
        url=reverse('index')
        print(resolve(url))
