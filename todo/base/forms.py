from django import forms

from .models import Task, User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')
