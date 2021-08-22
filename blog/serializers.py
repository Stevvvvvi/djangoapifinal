from authentication.serializers import UserRegisterSerializer
from django.db.models import fields
from blog.models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    owner = UserRegisterSerializer(many=False, read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'tags', 'owner', 'created', 'modified']
        read_only_fields = ['owner', 'created', 'modified']