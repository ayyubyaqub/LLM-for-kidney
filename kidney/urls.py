from django.urls import path
from .views import UploadPage,TaskUploadAPIView

urlpatterns = [

    path(
        "",
        UploadPage.as_view(),
        name="home"
    ),

    path(
        "upload-task/",
        TaskUploadAPIView.as_view(),
        name="upload-task"
    ),

]