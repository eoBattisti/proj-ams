from decimal import Decimal

from django.forms import DecimalField, ModelForm

from tasks.models import Task, TaskType


class TaskForm(ModelForm):
    value = DecimalField(min_value=0, max_digits=10, decimal_places=2, initial=0)

    class Meta:
        model = Task
        fields = ["description", "value", "task_type"]

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
    base_value = DecimalField(min_value=0, max_digits=10, decimal_places=2, initial=0)

    class Meta:
        model = TaskType
        fields = ["description", "base_value"]
