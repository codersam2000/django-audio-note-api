from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

class registerAPIView(APIView):
    def post(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        password2 = request.data.get('password2')
        # terms = request.data.get('terms')
        # password = validated_data['password']
        # password2 = self.initial_data.get('password2')
        # if terms != 'on':
        #     return Response({'type':'error','message':'Agree to terms and conditions.'})
        if not username or not email or not password or not password2:
            return Response({'type':'error','message':'Required fields are empty!'})
        elif password != password2:
            return Response({'type':'error','message':'Password not matched!'})
        elif User.objects.filter(username=username).exists():
            return Response({'type':'error','message':'User already exists!'})
        elif User.objects.filter(email=email).exists():
            return Response({'type':'error','message':'Email already exist!'})
        else:
            user = User.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                username=username, 
                email=email, 
                )
            user.set_password('password')
            user.save()
            user = User.objects.get(username=username)
            token = Token.objects.get_or_create(user=user)
            userSerializer = UserSerializer(user)
            return Response({'type':'success','token': str(token[0]),'user': userSerializer.data})  
    

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        checkUser = User.objects.filter(username=username)
        if not checkUser:
            return Response({'type':'error','message':'User does not exist!'})
        
        user = User.objects.get(username=username)
        print(authenticate(username=username, password=password))
        # if not authenticate(username=username, password=password):
        #     return Response({'type':'error','message':'Incorrect password!'})
        
        token = Token.objects.get_or_create(user=user)
        userSerializer = UserSerializer(user)
        return Response({'type':'success','token': str(token[0]),'user': userSerializer.data})
    
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
       






    