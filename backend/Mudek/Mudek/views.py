# Django
from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse


def login_redirect(request):
    return redirect('/edms/login')


