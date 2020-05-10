from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =("username","password","first_name","last_name", 'email')
        def get_mybooking(self, instance):
            try:
                return user.objects.all()
            except:
               return None

class SeatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = seats
        fields = ['slot_name', 'visiname', 'status', 'date']

        def get_mybooking(self, instance):
            try:
                return seats.objects.filter(visiname= instance.user_name)
            except:
               return None

class allSeatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = allbookings
        fields = ['slot_name', 'visiname', 'status', 'date']

        def get_mybooking(self, instance):
            try:
                return allbookings.objects.all()
            except:
               return None
