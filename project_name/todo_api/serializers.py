from rest_framework import serializers
from .models import TodoTask

class TodoTask_Serializer(serializers.ModelSerializer):
  class Meta:
    model = TodoTask
    fields = ('title', )
