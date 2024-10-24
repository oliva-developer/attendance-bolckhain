from django.db import models

class Student(models.Model):
    dni = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    ciclo = models.CharField(max_length=1)

    def __str__(self):
        return self.dni
    
class Course(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Class(models.Model):
    course_id = models.IntegerField()
    date = models.CharField(max_length=150)
    time_start = models.CharField(max_length=10)
    time_end = models.CharField(max_length=10)

    def __str__(self):
        return self.course_id
    
class StudentAttendance(models.Model):
    class_id = models.IntegerField()
    student_id = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    ciclo = models.CharField(max_length=1)

    def __str__(self):
        return self.class_id