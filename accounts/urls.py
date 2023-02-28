from django.urls import path
from accounts.views import UserCreateAPIView, UserLoginAPIView, UserDestroyView

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view()),
    path('signin/', UserLoginAPIView.as_view()),
    path('delete/', UserDestroyView.as_view()),
]