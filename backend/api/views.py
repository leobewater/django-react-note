from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Note
from .serializers import NoteSerializer, UserSerializer


class NoteListCreate(generics.ListCreateAPIView):
    # return list of notes or create a new note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # override default get_queryset
    def get_queryset(self):
        # get all notes of the user
        user = self.request.user
        return Note.objects.filter(author=user)

    # override and add author when create note
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # override default get_queryset
    def get_queryset(self):
        # get all notes of the user
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
