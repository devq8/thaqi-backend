from django.urls import path
from chatbot.views import ChatRetrieveView, MessageRetrieveView

urlpatterns = [
    path('chats/<int:user_id>/', ChatRetrieveView.as_view()),
    path('messages/<int:chat_id>/', MessageRetrieveView.as_view()),
]