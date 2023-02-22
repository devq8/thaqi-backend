from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from chatbot.permissions import IsOwnerChat, IsOwnerMessage
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatbot.models import Chat, Message
from chatbot.serializers import ChatListSerializer, ChatCRUDSerializer, MessageListSerializer, MessageCRUDSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_502_BAD_GATEWAY
import openai
import environ
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

env = environ.Env()

openai.api_key = env('OPENAI_API_KEY')

# ###################################################
# #################   Chat Views   ##################
# ###################################################

class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer
    permission_classes = [IsAuthenticated|IsOwnerChat]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(user=user).order_by('-created_at')
    
class ChatCreateView(CreateAPIView):
    serializer_class = ChatCRUDSerializer
    permission_classes = [IsAuthenticated]

    # We added perform_create() function just to assign a user to the new instance created.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatCRUDSerializer
    permission_classes = [IsOwnerChat]
    lookup_field = 'id'
    lookup_url_kwarg = 'chat_id'

class ChatDestroyView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatCRUDSerializer
    permission_classes = [IsOwnerChat]
    lookup_field = 'id'
    lookup_url_kwarg = 'chat_id'

# ###################################################
# ##############   Message Views   ##################
# ###################################################

class MessageListView(ListAPIView):
    serializer_class = MessageListSerializer
    lookup_field = 'chat'
    lookup_url_kwarg = 'chat_id'
    permission_classes = [IsAuthenticated|IsOwnerMessage]

    def get_queryset(self):
        try:
            chat_id = self.kwargs.get(self.lookup_url_kwarg)
            chat = Chat.objects.get(id=chat_id)
            if chat.user != self.request.user:
                raise PermissionDenied("You are not the owner of this chat.")
            queryset = Message.objects.filter(chat=chat).order_by('created_at')
            
            print(f'We found {queryset.count()} messages under that chat ({chat}) in the system.')
            return queryset
        except Chat.DoesNotExist:
            print('Chat was not found!')
            return None

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset is None:
            return Response({'Error': 'Chat is not found!'}, status=HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
    lookup_field = 'chat'
    lookup_url_kwarg = 'chat_id'
    permission_classes = [IsAuthenticated, IsOwnerChat]

    def perform_create(self, serializer):
        chat_id = self.kwargs.get('chat_id')
        chat = get_object_or_404(Chat, id=chat_id)
        serializer.save(chat=chat)

class MessageUpdateView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCRUDSerializer
    permission_classes = [IsOwnerChat]
    lookup_field = 'id'
    lookup_url_kwarg = 'message_id'

class MessageDestroyView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCRUDSerializer
    permission_classes = [IsOwnerChat]
    lookup_field = 'id'
    lookup_url_kwarg = 'message_id'

def generate_answer(chat, prompt):
    
    model_engine = "text-davinci-003"
    history = ''
    for message in chat.messages.all():
        history += f'{message.message.strip()}\n\n{message.response.strip()}\n\n'
    
    prompt = f"{history}{prompt}"
    
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = completions.choices[0].text
    return answer