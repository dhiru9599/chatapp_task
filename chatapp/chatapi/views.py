#from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import User, Group, Message
from .serializers import UserSerializer, GroupSerializer, MessageSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupCreateView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDeleteView(generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupMemberAddView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

