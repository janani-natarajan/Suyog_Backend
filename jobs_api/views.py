from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

# View to return the list of jobs, filtered by department if requested
class JobList(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        # Grabs the department from the URL parameter (e.g., ?department=IT)
        department_query = self.request.query_params.get('department', '')
        
        if department_query:
            # Filters the database for jobs matching the department name
            return Job.objects.filter(department__icontains=department_query)
        
        return Job.objects.all()

# View to return a unique list of all departments for the Android Spinner
class DepartmentList(APIView):
    def get(self, request):
        # Fetches unique department names, removing nulls and empty strings
        departments = Job.objects.values_list('department', flat=True).distinct().exclude(department__isnull=True).exclude(department='')
        
        # Returns a sorted list of department names
        return Response(sorted(list(departments)))