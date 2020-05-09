from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =("username","password","first_name","last_name", 'email')

class SeatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = seats
        fields = ['slot_name', 'visiname', 'status', 'date']

        def get_mybooking(self, instance):
            try:
                return seats.objects.filter(visiname= instance.user_name)
            except:
               return None

class allSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = allbookings
        fields = ['slot_name', 'visiname', 'status', 'date']
