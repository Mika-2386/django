from django.urls import path

from rest_framework.routers import DefaultRouter

from todo import views

from todo.views import TaskModelViewSet

router = DefaultRouter()
router.register("tasks", TaskModelViewSet)



urlpatterns = [
    path("", views.index, name="index"),
    ]

urlpatterns.extend(router.urls)