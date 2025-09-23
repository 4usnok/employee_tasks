from django.urls import path

from . import views

app_name = "employee_table"

urlpatterns = [
    path('tables/', views.EmployeeTableList.as_view(), name="list-views"),
    path('tables/create/', views.EmployeeTableCreate.as_view(), name="tables-create"),
    path('tables/<int:pk>/destroy/', views.EmployeeTableDestroy.as_view(), name="tables-destroy"),
    path('tables/<int:pk>/update/', views.EmployeeTableUpdate.as_view(), name="tables-update"),
    path('tables/<int:pk>/', views.EmployeeTableRetrieve.as_view(), name="tables-detail"),
    path('active_task', views.EmployeeListWithActiveTasks.as_view(), name="active-task"),
]