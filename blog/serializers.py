from django.db.models import fields
from blog.models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'tags', 'owner', 'created', 'modified']
        read_only_fields = ['owner', 'created', 'modified']