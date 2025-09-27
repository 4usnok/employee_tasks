from django.urls import path

from . import views

app_name = "task_table"

urlpatterns = [
    path('tables/', views.TaskList.as_view(), name="list-views"),
    path('tables/create/', views.TaskTableCreate.as_view(), name="tables-create"),
    path('tables/<int:pk>/destroy/', views.TaskTableDestroy.as_view(), name="tables-destroy"),
    path('tables/<int:pk>/update/', views.TaskTableUpdate.as_view(), name="tables-update"),
    path('tables/<int:pk>/', views.TaskTableRetrieve.as_view(), name="tables-detail"),
    path('tables/active_task/', views.TaskListNotWork.as_view(), name="active-task"),
]