from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This tells Django to use the urls.py file inside the jobs_api folder
    path('', include('jobs_api.urls')), 
]