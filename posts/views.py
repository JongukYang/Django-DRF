from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import response
from .models import Post
from .serializers import PostModelSerializer


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
