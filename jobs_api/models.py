from django.db import models

class Job(models.Model):
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    group = models.CharField(max_length=100)
    nature_of_work = models.TextField()

    def __str__(self):
        return self.designation