from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm
from .utils import TaskRequiredMixin

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(user=user)
        return Task.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input
            )
        context['search_input'] = search_input
        return context


class TaskDetail(TaskRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk'


class TaskCreate(TaskRequiredMixin, CreateView):
    form_class = TaskForm
    template_name = 'base/task_create.html'

    def get_success_url(self) -> str:
        return reverse_lazy('base:task_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(TaskRequiredMixin, UpdateView):
    model = Task
    fields = ('title', 'description', 'complete')
    template_name = 'base/task_create.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self) -> str:
        return reverse_lazy('base:task_detail', kwargs={'pk': self.object.pk})


class TaskDelete(TaskRequiredMixin, DeleteView):
    model = Task
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('base:tasks')
    context_object_name = 'task'