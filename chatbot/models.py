from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chat(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chats',
    )
    title = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    message = models.TextField(blank=False, null=False)
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat.title
        
    @property
    def user(self):
        return self.chat.user