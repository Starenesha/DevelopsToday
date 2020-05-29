from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Post, Comment
from .serializers import PostListSerializer, CommentListSerializer


class PostCreateApiView(generics.CreateAPIView):
    serializer_class = PostListSerializer


class PostsApiView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class CommentApiView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()


class CommentCreateApiView(generics.CreateAPIView):
    serializer_class = CommentListSerializer


class CommentUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()
