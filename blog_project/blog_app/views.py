from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from .permission import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here....
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


def perform_create(self, serializer):
    serializer.save(author=self.request.user)