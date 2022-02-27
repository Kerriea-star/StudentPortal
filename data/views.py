from rest_framework import generics
from .serializers import StudentSerializer
from .permissions import IsStudentOrReadOnly # Imported our permission
from .models import Student

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsStudentOrReadOnly,) # new
    queryset = Student.objects.all()
    serializer_class = StudentSerializer