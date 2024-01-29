from rest_framework import generics, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tasks.services import TaskService
from tasks.permissions import IsOwner
from tasks.models import Task
from tasks.filters import TaskFilter
from tasks.serializers import TaskSerializer
import logging

logger = logging.getLogger(__name__)


class TaskListCreateView(generics.ListCreateAPIView):
    """
    Thought this endpoint you can create a task and retrieve a list of them. Using
    filters for retrieving:
        - Create a single Task:
            Params: {
                "content": "Dummy content"
                }
            Response: 201
        - Retrieve a list:
            Available filters:
                - content: string
                - completed: boolean
                - created_at__gte: datetime
                - created_at__lte: datetime
    """

    serializer_class = TaskSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        logger.info(
            f"New Task created with id: {instance.id} from the user {self.request.user.id}"
        )


class TaskViewSet(viewsets.ModelViewSet):
    """
    This endpoint has two functions:
        - Delete a Task.
        - Retrieve a single Task.
        - Mark as completed a single Task.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    @action(detail=True, methods=["put"])
    def mark_as_completed(self, request, pk=None):
        task = self.get_object()
        try:
            task = TaskService.mark_as_completed(task)
        except Exception as e:
            return Response(
                {"error": f"Tasks could not be mark as completed: {e}"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = self.get_serializer(task)
        return Response(serializer.data)
