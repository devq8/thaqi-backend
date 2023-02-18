from django.urls import path
from chatbot.views import ChatListView, ChatCreateView, ChatUpdateView, ChatDestroyView
from chatbot.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDestroyView

urlpatterns = [
    ############### Chats ###############
    path('chats/', ChatListView.as_view(), name='chat_list'),
    path('chats/create/', ChatCreateView.as_view(), name='new_chat'),
    path('chats/<int:chat_id>/update/', ChatUpdateView.as_view(), name='update_chat'),
    path('chats/<int:chat_id>/delete/', ChatDestroyView.as_view(), name='delete_chat'),

    ############# Messages #############
    path('chats/<int:chat_id>/messages/', MessageListView.as_view(), name='message_list'),
    path('chats/<int:chat_id>/messages/create/', MessageCreateView.as_view(), name='new_message'),
    path('chats/<int:chat_id>/messages/<int:message_id>/update/', MessageUpdateView.as_view(), name='update_message'),
    path('chats/<int:chat_id>/messages/<int:message_id>/delete/', MessageDestroyView.as_view(), name='delete_message'),
]