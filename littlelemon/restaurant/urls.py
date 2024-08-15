from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
  path('menu/', views.MenuView.as_view(), name='menu-list'),
  path('menu/<int:pk>', views.SingleMenuView.as_view()),
  path('api-token-auth/', obtain_auth_token),
  path('bookings/', views.BookingViewSet.as_view({'get': 'list'})),
  path('registration/', views.UserViewSet.as_view({'get': 'list'})),
]