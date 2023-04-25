from django.db import models

# Create your models here.


class Student(models.Model):
    Studentname = models.CharField(max_length=255)
    studentemail = models.EmailField()
    phone = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=255,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    coursename = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Enrollment(models.Model):
    ENROLLED = 'enrolled'
    DROPPED = 'dropped'
    STATUS_CHOICES = [
        (ENROLLED,'Enrolled'),
        (DROPPED,'Dropped'),
    ]

    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=8,choices=STATUS_CHOICES,default=ENROLLED)
    created_at = models.DateTimeField(auto_now_add=True)

class Instructor(models.Model):
    Instructorname = models.CharField(max_length=255)
    Instructoremail = models.EmailField()
    Instphone = models.ForeignKey
        