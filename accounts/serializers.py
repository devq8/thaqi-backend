from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',]

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def create(self, validated_data):
        print('Create new user process started ...')
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        print('User created successfully!')

        payload = RefreshToken.for_user(new_user)
        payload['username'] = str(new_user.username)
        token = str(payload.access_token)
        validated_data['token'] = token
        print(validated_data)
        
        return validated_data

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError('This user does not exist!')
        if not user_obj.check_password(my_password):
            raise serializers.ValidationError('Incorrect password!')
        
        payload = RefreshToken.for_user(user_obj)
        payload['username'] = user_obj.username
        token = str(payload.access_token)
        
        data['token'] = token

        return data
