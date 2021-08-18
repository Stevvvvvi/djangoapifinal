from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserRegisterView.as_view()),
    path('login/',views.UserLoginView.as_view()),
]
