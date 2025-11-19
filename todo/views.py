from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import viewsets

from todo.models import Task
from todo.serializers import TaskSerializer


def index(request):
    return HttpResponse(" Веб-приложение для управления Задачами")


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = TaskSerializer