from rest_framework import viewsets
from .models import Course, Student, Class, StudentAttendance
from .serializers import StudentSerializer, ClassSerializer, StudentAttendanceSerializer, CourseSerializer
from web3 import Web3

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = []

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    permission_classes = []
    

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    permission_classes = []

class StudentAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StudentAttendance.objects.all()
    serializer_class = StudentAttendanceSerializer

    permission_classes = []