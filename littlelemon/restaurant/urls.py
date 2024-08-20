from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
  path('about/', views.about, name="about"),
  path('book/', views.book, name="book"),
  path('reservations/', views.reservations, name="reservations"),
  path('', views.index, name='index'),
  path('menu/', views.menu, name="menu"),
  path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
  path('bookings/', views.bookings, name="bookings"),
  path('api-token-auth/', obtain_auth_token),
  path('registration/', views.UserViewSet.as_view({'get': 'list'})),
  
]