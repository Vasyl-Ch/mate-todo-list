from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="home"),
    path("task/add/", views.TaskCreateView.as_view(), name="task_add"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/toggle/", views.ToggleTaskView.as_view(), name="task_toggle"),
    path("tags/", views.TagListView.as_view(), name="tags"),
    path("tags/add/", views.TagCreateView.as_view(), name="tag_add"),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag_delete"),
]
