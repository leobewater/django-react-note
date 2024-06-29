from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # serialize these fields
        fields = ['id', 'username', 'password']
        # accept password when create user
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        # can't write author via API, read only
        extra_kwargs = {'author': {'read_only': True}}
