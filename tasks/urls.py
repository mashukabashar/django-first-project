from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, test, create_task, view_task, update_task, delete_task, task_details


urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('employee-dashboard/', employee_dashboard, name="employee-dashboard"),
    path('task/<int:task_id>/details/', task_details, name='task-details'),
    path('view_task/', view_task),
    ]


# source task_env/bin/activate