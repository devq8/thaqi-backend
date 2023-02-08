from django.urls import path
from accounts.views import UserCreateAPIView, UserLoginAPIView

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view()),
    path('signin/', UserLoginAPIView.as_view()),
]