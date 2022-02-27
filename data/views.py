from rest_framework import generics, permissions # new (imported permissions from rest framework) 
from .serializers import StudentSerializer
from .models import Student

class StudentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Student.objects.all()
    serializer_class = StudentSerializer