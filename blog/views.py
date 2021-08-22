from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.serializers import BlogSerializer
from blog.models import Blog
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet

# Create your views here.
# class BlogView(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     permission_classes = [IsAuthenticated]
#     def get_queryset(self):
#         assert self.queryset is not None, (
#             "'%s' should either include a `queryset` attribute, "
#             "or override the `get_queryset()` method."
#             % self.__class__.__name__
#         )

#         queryset = self.queryset.filter(owner=self.request.user)
#         if isinstance(queryset, QuerySet):
#             # Ensure queryset is re-evaluated on each request.
#             queryset = queryset.all()
#         return queryset

class BlogView(ListCreateAPIView):
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class BlogDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Blog.objects.filter(owner=self.request.user)