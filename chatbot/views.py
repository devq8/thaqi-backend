from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from chatbot.models import Chat, Message
from chatbot.serializers import ChatSerializer, MessageSerializer

class ChatRetrieveView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user_id'

class MessageRetrieveView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'chat'
    lookup_url_kwarg = 'chat_id'