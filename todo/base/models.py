from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200, verbose_name='Title', help_text='Set a title')
    description = models.TextField(null=True, help_text='Add descriprion')
    complete = models.BooleanField(default=False, help_text='Task is complete ?')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('complete', '-created')