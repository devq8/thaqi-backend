from rest_framework.permissions import BasePermission
from chatbot.models import Chat, Message, User
from django.shortcuts import get_object_or_404

class IsOwnerChat(BasePermission):
    message = 'Access denied!'

    def has_permission(self, request, view):
        chat_id = view.kwargs.get('chat_id')
        chat = get_object_or_404(Chat, id=chat_id)
        return chat.user == request.user
        # return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if the object is Chat, then it will check if the user is owner
        print('HasObjectPermission function is called')
        if isinstance(obj, Chat):
            print('Check Chat permission')
            if  obj.user == request.user:
                print('User has permission to delete')
            else:
                print('User is not authorized to delete')
            return obj.user == request.user
        elif isinstance(obj, Message):
            print('Check Message permission')
            return obj.chat.user == request.user
        return False
        
class IsOwnerMessage(BasePermission):
    message = 'Access denied!'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if the object is Message, then it will check if the user is owner
        if isinstance(obj, Message):
            return obj.chat.user == request.user
        return obj.chat.user == request.user
        