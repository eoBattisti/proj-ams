from decimal import Decimal

from django import forms
from django.forms import ModelForm
from tasks.models import Task
from tasks.models import TaskType


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["description", "value", "task_type"]
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control", "autofocus": True}),
            "value": forms.NumberInput(attrs={"class": "form-control", "value": 0, "min": 0, "step": 1}),
            "task_type": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance: Task

    def clean(self):
        cleaned_data = super().clean()

        value: Decimal = cleaned_data.get("value")
        task_type: TaskType = cleaned_data.get("task_type")

        # We validate if the value for the Task is not provided,
        # we set it to the base value of the TaskType
        if value == 0 and task_type:
            cleaned_data["value"] = task_type.base_value

        return cleaned_data


class TaskTypeForm(ModelForm):
    class Meta:
        model = TaskType
        fields = ["description", "base_value"]
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control", "autofocus": True}),
            "base_value": forms.NumberInput(attrs={"class": "form-control", "value": 0, "min": 0, "step": 1}),
        }
