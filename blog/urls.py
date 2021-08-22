from blog.views import BlogView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BlogView)

urlpatterns = [
    path('',include(router.urls))
]
