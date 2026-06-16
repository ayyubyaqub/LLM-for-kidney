from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name


class TaskImage(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="kidney_images/"
    )

    prediction = models.IntegerField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)