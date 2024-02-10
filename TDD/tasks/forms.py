from django.forms import ModelForm
from .models import Task

class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']