from django.urls import path
from .views import JobList, DepartmentList  # This imports from jobs_api.views

urlpatterns = [
    path('api/jobs/', JobList.as_view(), name='job-list'),
    path('api/departments/', DepartmentList.as_view(), name='department-list'),
]