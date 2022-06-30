from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework import generics

from todo.forms import CreateUserForm, CreateTaskForm
from todo.models import Task
from todo.serializers import TaskSerializer


class GetTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def order_app(request):
    return render(request, 'main.html')


# @allowed_users(allowed_roles=['admin'])
def registerPage(request):
    """Регистрация"""
    form = CreateUserForm()
    error = ""
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, 'Пользователь ' + username + ' был создан')

            return redirect('/api/v1/login')
        else:
            error = form.errors
            print(error)

    context = {"form": form, 'error':error}
    return render(request, 'register.html', context)


# @unauthenticated_user
def loginPage(request):
    """Авторизация"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/api/v1/todo_list")
        else:
            messages.info(request, 'Логин или пароль введен не верно')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/api/v1/login')


def todo_list(request):
    tasks = Task.objects.filter(owner_id=request.user.id)
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(title=task, owner_id=request.user.id)
    context = {
        'tasks':tasks
    }
    return render(request, 'todo_list.html', context)


class SingleTask(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AddTask(generics.CreateAPIView):
    serializer_class = TaskSerializer


class UpdateTask(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()