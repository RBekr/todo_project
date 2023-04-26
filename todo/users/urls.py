from django.urls import path
from django.contrib.auth.views import (PasswordResetDoneView,
                                       PasswordChangeDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)

from .views import SignUpView, UserLoginView, PasswordsChangeView, logout_user, password_reset

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/',
         logout_user,
         name='logout'),
    path('login/',
         UserLoginView.as_view(),
         name='login'),
    path('password_change/form/',
          PasswordsChangeView.
          as_view(template_name='users/password_change_form.html'),
          name='password_change_form'),
    path('password_change/done/',
         PasswordChangeDoneView.
         as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/form/',
         password_reset,
         name='password_reset_form'),
    path('password_reset/done/',
         PasswordResetDoneView.
         as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.
         as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.
         as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

     ]
