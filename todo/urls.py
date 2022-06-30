from django.urls import path
from .views import *

urlpatterns = [

    # Авторизация

    path('login/', loginPage, name="loginPage"),
    path('logout/', logoutUser),
    path('register/', registerPage, name="registerPage"),
    ##
    path("", GetTasks.as_view()),
    path("<int:pk>", SingleTask.as_view()),
    path('task', AddTask.as_view()),
    path('<int:pk>/update', UpdateTask.as_view()),
    path('page', order_app),
    path('todo_list', todo_list,)
]