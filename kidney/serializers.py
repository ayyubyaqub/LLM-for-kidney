from rest_framework import serializers
from .models import Task, TaskImage


class TaskImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskImage
        fields = [
            "id",
            "image",
            "prediction",
            "created_at"
        ]


class TaskSerializer(serializers.ModelSerializer):

    images = TaskImageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Task
        fields = [
            "id",
            "task_name",
            "created_at",
            "images"
        ]