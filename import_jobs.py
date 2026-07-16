import os
import django
import csv

# Set up the Django environment so this script can talk to your database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from jobs_api.models import Job

def import_csv():
    # Make sure the file name matches your actual CSV file
    file_path = 'jobs.csv' 
    
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        count = 0
        for row in reader:
            # Create a new Job entry in the database for every row in the CSV
            Job.objects.create(
                designation=row.get('Designation', ''),
                department=row.get('Department', ''),
                group=row.get('Group', ''),
                nature_of_work=row.get('  Nature of work', '') # Matching your exact CSV column name
            )
            count += 1
            
        print(f"Successfully imported {count} jobs into the database!")

if __name__ == '__main__':
    import_csv()