from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    regNo = models.IntegerField(default=0, null=True, blank=True)
    course = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    period = models.IntegerField(default=0, blank=True, null=True)
    current_year = models.DateTimeField(auto_now_add=True)
    current_semester = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name