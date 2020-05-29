from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PostCreateApiView, PostsApiView, PostUpdateApiView, CommentCreateApiView, \
    CommentApiView, CommentUpdateApiView


app_name = "news"

urlpatterns = [
    path('posts/create/', PostCreateApiView.as_view()),
    path('posts/', PostsApiView.as_view()),
    path('posts/update/<int:pk>', PostUpdateApiView.as_view()),
    path('comments/', CommentApiView.as_view()),
    path('comments/create', CommentCreateApiView.as_view()),
    path('comments/update/<int:pk>', CommentUpdateApiView.as_view()),
]

