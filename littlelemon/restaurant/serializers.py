from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory', 'description']

class BookingSerializer(serializers.ModelSerializer):
   class Meta:
      model = Booking
      fields = '__all__'

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'groups']