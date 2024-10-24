from rest_framework import serializers
from .models import Student, Class, StudentAttendance, Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        # Campos que tendrán reglas adicionales (ej. solo escritura)
        # extra_kwargs = {
        #     'ciclo': {'read_only': True}   # No se puede modificar directamente
        # }

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

