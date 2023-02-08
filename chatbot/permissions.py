from rest_framework.permissions import BasePermission
from chatbot.models import Chat, Message

class IsOwner(BasePermission):
    message = 'Access denied!'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    # def has_object_permission(self, request, view, obj):
    #     chat = Chat.objects.get(user = request.user)
    #     if obj in 
    #         return True