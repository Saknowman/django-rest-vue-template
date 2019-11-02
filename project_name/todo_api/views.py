from rest_framework import viewsets
from .models import TodoTask
from .serializers import TodoTask_Serializer


class TodoTask_ViewSet(viewsets.ModelViewSet):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTask_Serializer
