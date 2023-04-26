from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from .forms import LoginUserForm, UserCreateForm

User = get_user_model()
class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('base:tasks')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

def logout_user(request):
    logout(request)
    return redirect('/')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')


@csrf_exempt
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)

            if user:
                send_msg(request, user, 'Тема письма', 'Текст письма.',
                         email, fail_silently=False)
                return redirect('users:password_reset_done')
        else:
            return redirect('users:password_reset_form')

    form = PasswordResetForm()
    return render(request, 'users/password_reset_form.html', {'form': form})

def send_msg(request, user, theme, text, email, fail_silently):
    subject = theme
    token = default_token_generator.make_token(user)
    uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
    relativelink = f'/auth/reset/{uidb64}/{token}'

    current_site = get_current_site(request=request).domain
    absurl = 'http://' + current_site + relativelink
    email_body = ('Hello, \n Use link below to reset your password  \n'
                  + absurl)
    body = f'''{text}
               email: {email}
               token: {token}
               link: {email_body}
            '''

    from_email = 'yatube@example.com'

    send_mail(
        subject, body, from_email, [email], fail_silently=fail_silently,
    )