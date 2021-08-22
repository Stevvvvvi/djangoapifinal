from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('',views.getUserDetail),
    path('', views.UserRegisterView.as_view()),
    # path('', views.UserRegisterView.as_view({'get': 'getUserDetail','post':'post'})),
    path('login/',views.UserLoginView.as_view()),

    
]
