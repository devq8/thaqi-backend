from rest_framework import serializers
from chatbot.models import Chat, Message
from accounts.serializers import UserSerializer


class MessageListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['id', 'message', 'response', 'created_at']
        ordering = ['created_at']

class MessageCRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['message', 'response']
        

class ChatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ['id', 'user', 'title', 'created_at',]
        ordering = ['-created_at']

class ChatCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = [ 'title',]

