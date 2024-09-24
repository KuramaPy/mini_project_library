from django.urls import path , include
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, delete_filtered_books

app_name = "manage_book"

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('delete_filtered/', delete_filtered_books, name='task_delete_filtered'), 
    path('<int:pk>/', include([
        path('update/', TaskUpdateView.as_view(), name='task_update'),
        path('delete/', TaskDeleteView.as_view(), name='task_delete'),
        path('detail/', TaskDetailView.as_view(), name='task_detail'),
    ])),
]