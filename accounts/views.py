from accounts.models import User
from rest_framework.generics import CreateAPIView, DestroyAPIView
from accounts.serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            print('User logged in successfully!')
            return Response(valid_data, status=HTTP_200_OK)
        return Response(valid_data, status=HTTP_400_BAD_REQUEST)
    
class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user