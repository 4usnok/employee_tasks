from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("employee_table/", include('employee_table.urls')),
    path("task_table/", include('task_table.urls')),
    path("admin/", admin.site.urls),
]
