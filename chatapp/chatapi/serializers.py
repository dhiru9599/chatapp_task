from rest_framework import serializers
from .models import User, Group, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [ 'name', 'members']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [ 'group', 'sender', 'content', 'likes']
