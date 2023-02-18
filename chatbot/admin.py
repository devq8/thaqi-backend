from django.contrib import admin
from chatbot.models import Chat, Message

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin): 
    fields = ('user', 'title', )
    list_display = ('id', 'title', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    ordering = ('created_at',)
    search_fields = ('user', 'title')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin): 
    fields = ('chat', 'message', 'response')
    list_display = ('id', 'chat', 'user', 'message', 'response')
    list_filter = ('chat', 'created_at')
    ordering = ('created_at',)
    search_fields = ('chat',)
