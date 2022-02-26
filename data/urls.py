from django.urls import path
from .views import StudentList, StudentDetail

urlpatterns = [
    path('<int:pk>/', StudentDetail.as_view()),
    path('', StudentList.as_view()),
]