from django.contrib import admin
from tasks.models import Task
from tasks.models import TaskType

admin.site.register(Task)
admin.site.register(TaskType)
