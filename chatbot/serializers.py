from rest_framework import serializers
from chatbot.models import Chat, Message
from accounts.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['id', 'chat', 'message', 'direction', 'created_at']
        ordering = ['created_at']

class ChatSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    # messages = MessageSerializer()

    class Meta:
        model = Chat
        fields = ['id', 'user', 'title', 'created_at', 'messages']
        ordering = ['-created_at']
