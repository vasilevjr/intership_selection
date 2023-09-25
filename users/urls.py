from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import TaskViewsSet


router = DefaultRouter()
router.register(r'tasks', TaskViewsSet, basename='task')


urlpatterns = [
    path('', include(router.urls))
]