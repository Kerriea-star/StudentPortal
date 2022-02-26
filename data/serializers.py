from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'regNo', 'course', 'department', 'school', 'period', 'current_year', 'current_semester',)
        model = Student