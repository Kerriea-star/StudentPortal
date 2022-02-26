from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student

class StudentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user (student)
        teststudent1 = User.objects.create_user(
            username='teststudent', password='abc123')
        teststudent1.save()

        # Add other details
        details = Student.objects.create(
            name='teststudent', regNo=1234, course="Bachelor of Science In Information Technology",
            department="Informatics and Computing", school="Science and Informatics",
            period=4, current_semester=1)
        details.save()

    def test_student_details(self):
        student = Student.objects.get(id=1)
        name = f'{student.name}'
        regNo=f'{student.regNo}'
        course = f'{student.course}'
        department = f'{student.department}'
        school = f'{student.school}'
        period = f'{student.period}'
        current_semester = f'{student.current_semester}'
        self.assertEqual(name, 'teststudent')
        self.assertEqual(regNo, '1234')
        self.assertEqual(course, 'Bachelor of Science In Information Technology')
        self.assertEqual(department, 'Informatics and Computing')
        self.assertEqual(school, 'Science and Informatics')
        self.assertEqual(period, '4')
        self.assertEqual(current_semester, '1')