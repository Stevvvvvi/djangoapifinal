from django.contrib.admin.options import ModelAdmin
from blog.models import Blog
from django.contrib import admin

# Register your models here.
@admin.register(Blog)
class MyBlogs(ModelAdmin):
    ordering = ('-created',)
    list_display = ('id', 'title', 'content', 'tags', 'owner', 'created', 'modified')