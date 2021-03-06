from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users2', views.UserViewSet)

urlpatterns = [
    path('users', views.userlist, name = 'users'),
     path('', include (router.urls))
]