from django.contrib import admin
from django.urls import path, include
from django.urls import path
from task.views import TaskListView, TaskDetailView, TaskCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
]
urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
]
