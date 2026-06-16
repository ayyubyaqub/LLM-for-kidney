from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kidney.serializers import TaskImageSerializer ,TaskSerializer
from .models import Task, TaskImage
# from .ai_model import predict_kidney
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class TaskUploadAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    def get(self, request):
        task_objects=Task.objects.all().order_by('-id')
        serializer=TaskSerializer(task_objects,many=True)
        return Response(serializer.data)

    def post(self, request):

        task_name = request.data.get("task_name")

        images = request.FILES.getlist("images")

        if not task_name:
            return Response(
                {"error": "Task name is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not images:
            return Response(
                {"error": "Please upload images"},
                status=status.HTTP_400_BAD_REQUEST
            )

        task = Task.objects.create(
            task_name=task_name
        )

        results = []
        from random import randint
        for image_file in images:

            prediction = randint(1,3)

            obj = TaskImage.objects.create(
                task=task,
                image=image_file,
                prediction=prediction
            )

            results.append({
                "id": obj.id,
                "image_name": image_file.name,
                "prediction": prediction
            })

        return Response({
            "success": True,
            "task_id": task.id,
            "task_name": task.task_name,
            "results": results
        })
    


from django.shortcuts import render
from django.views import View


class UploadPage(View):

    def get(self, request):

        return render(
            request,
            "upload_task.html"
        )