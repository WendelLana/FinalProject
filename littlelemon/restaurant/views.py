from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

# Create your views here.
class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]
  
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]