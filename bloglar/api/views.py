from rest_framework import generics

from bloglar.api.permissions import IsBlogSahibiOrReadOnly
from bloglar.api.serializers import BlogSerializer
from bloglar.models import Blog


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsBlogSahibiOrReadOnly]

