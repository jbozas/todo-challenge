from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskListCreateView, TaskViewSet

router = DefaultRouter()
router.register("", TaskViewSet, basename="tasks")

urlpatterns = [
    path("", include(router.urls)),
    path("list", TaskListCreateView.as_view(), name="task-list-create"),
]
