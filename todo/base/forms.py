from django import forms

from .models import Task, User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class': 'required form-check-input'})
        }


class TaskCompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['complete']
        