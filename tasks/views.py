from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return only tasks belonging to the logged-in user.
        Optionally filter by completion status:
        ?completed=true or ?completed=false
        """
        queryset = Task.objects.filter(user=self.request.user)

        is_completed = self.request.query_params.get("completed")
        if is_completed is not None:
            queryset = queryset.filter(
                is_completed=is_completed.lower() == "true"
            )

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Ensure users can only retrieve/update/delete their own tasks.
        """
        return Task.objects.filter(user=self.request.user)
