from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, StudentViewSet, ClassViewSet, StudentAttendanceViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'class', ClassViewSet)
router.register(r'student-attendances', StudentAttendanceViewSet)
