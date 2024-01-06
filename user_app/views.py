# django imports
import json
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models import Q

# rest_framework imports
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# in app imports
from user_app.serializers import (
    TokenSerializer,
    UserRegistrationSerialzier
)

# Create your views here.


#-------------------------------------------------------------------------------
#                              UserRegistrationMV
#-------------------------------------------------------------------------------


class UserRegistrationMV(viewsets.ModelViewSet):
    serializer_class = UserRegistrationSerialzier
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'put']

    def create(self, request, *args, **kwargs):
        data = request.data
        email = data['email']
        username = data['username']
        password = data['password']
        password2 = data['password2']

        if User.objects.filter(Q(email=email) | Q(username=username)).exists():
            return Response({'error': 'email already exists'}, status=400)
        
        if password != password2:
            return Response({'error': 'passwords did not match'}, status=400)
        
        account = User(
            username = username,
            email = email
        )
        account.set_password(password)
        account.save()
        Token.objects.create(user=account)

        user_data = {
            'message': 'User registered successfully!',
            'user': {
                'username': account.username,
                'email': account.email,
                'auth_token': account.auth_token.key
            }
        }
        return Response(data=user_data, status=201)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        username = data['username']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        is_user_exists = User.objects.filter(
            Q(email = email)
            | Q(username = username)
        ).exclude(
            Q(email = instance.email)
            | Q(username = instance.username)
        ).exists()

        if is_user_exists:
            return Response({'error': 'email already exists'}, status=400)
        
        if password != password2:
            return Response({'error': 'passwords did not match'}, status=400)

        instance.username = username
        instance.email = email
        instance.set_password(password)
        instance.save()

        user_data = {
            'message': 'User updated successfully!',
            'user': {
                'username': instance.username,
                'email': instance.email,
                'auth_token': instance.auth_token.key
            }
        }

        return Response(user_data, status=200)
    

#---------------------------------------------------------------------------
#                            UserLogoutMV
#---------------------------------------------------------------------------


class UserLogoutMV(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Token.objects.filter(user = self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        try:
            user_token = self.get_queryset()
            user_token.delete()
            data = {"message": "Token deleted successfully!"}
            return Response(data=data, status=204)
        except Exception as e:
            data = {"message": "Token does not exists!"}
            return Response(data=data, status=204)