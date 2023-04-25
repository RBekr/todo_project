from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from .models import Task
from .forms import TaskCompleteForm, TaskForm
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


class TaskCompleteView(FormView):
    form_class = TaskCompleteForm
    success_url = reverse_lazy('base:tasks')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        task = get_object_or_404(Task, id=self.kwargs['pk'])
        task.complete = not task.complete
        task.save()
        return super().form_valid(form)


class TaskDetail(TaskRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk'


class TaskCreate(TaskRequiredMixin, CreateView):
    form_class = TaskForm
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('base:tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(TaskRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'base/task_create.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('base:tasks')

class TaskDelete(TaskRequiredMixin, DeleteView):
    model = Task
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('base:tasks')
    context_object_name = 'task'