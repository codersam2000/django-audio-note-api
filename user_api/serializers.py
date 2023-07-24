from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


#serializers
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.CharField(read_only=True)
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise serializers.ValidationError("Unable to log in with provided credentials.")
        user - User.objects.get(username=username)
        token= Token.objects.get_or_create(user=user)
        
        attr = {
            "user":user,
            "token":token
        }
        return attrs
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'username']
        extra_kwargs = {'password2': {'write_only': True, 'required': False}, 'username': {'required': False},}
        depth = 1
        