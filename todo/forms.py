from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from todo.models import Task


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'