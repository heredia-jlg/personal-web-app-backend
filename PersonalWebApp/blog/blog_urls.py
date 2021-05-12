from django.urls import path
from .views import PostList

urlpatterns = [
    path('posts/all', PostList.as_view()),
    path('posts/insertPost', PostList.as_view())
]