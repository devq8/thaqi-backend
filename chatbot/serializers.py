from rest_framework import serializers
from chatbot.models import Chat, Message

from accounts.serializers import UserSerializer


class ChatSerializer(serializers.ModelSerializer):
    
    user = UserSerializer

    class Meta:
        model = Chat
        fields = ['user', 'title', 'created_at']
        ordering = ['-created_at']

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['chat', 'direction', 'created_at']
        ordering = ['created_at']