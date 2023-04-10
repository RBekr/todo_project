from django.contrib.auth.mixins import LoginRequiredMixin

class TaskRequiredMixin(LoginRequiredMixin):
    raise_exception = False