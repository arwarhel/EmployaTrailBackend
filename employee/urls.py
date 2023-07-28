from .views import EmployeeViewSet
from django.urls import path

employee_list = EmployeeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

employee_detail = EmployeeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

app_name = "employee"

urlpatterns = [
    path('employees/', employee_list, name='employee-list'),
    path('employees/<str:id>/', employee_detail, name='employees-detail')
]
