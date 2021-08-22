from blog.views import BlogView, BlogDetailView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', BlogView)

urlpatterns = [
    # path('',include(router.urls))
    path('',BlogView.as_view()),
    path('<int:id>/', BlogDetailView.as_view())
]

