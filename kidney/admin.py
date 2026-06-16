from django.contrib import admin

# Register your models here.
from kidney.models import *

admin.site.register(Task)
admin.site.register(TaskImage)