from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    name = models.CharField(max_length=512)
    gender = models.CharField(max_length=512)
    class_stream = models.CharField(max_length=512)
    class_year = models.CharField(max_length=512)
    email = models.EmailField()
    mobile = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.name} {self.email}"


class Question(models.Model):
    q = models.CharField(max_length=512)
    opt1 = models.CharField(max_length=256)
    opt2 = models.CharField(max_length=256)
    opt3 = models.CharField(max_length=256)
    opt4 = models.CharField(max_length=256)
    ans = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.q} {self.ans}"


class Response(models.Model):
    u = models.ForeignKey(Student, on_delete=models.CASCADE)
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    res = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.u.email} {self.res}"


class Notes(models.Model):
    title = models.CharField(max_length=256)
    cstream = models.CharField(max_length=256)
    cyear = models.CharField(max_length=256)
    notes = models.FileField(upload_to="pdfs")

    def __str__(self):
        return f'{self.title}'


class Assignment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    q = models.CharField(max_length=256)
    sub = models.CharField(max_length=256)
    cstream = models.CharField(max_length=256)
    cyear = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.q}'


class AssignmentResponse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    assres = models.FileField(upload_to="assignment_responses")
    
    def __str__(self):
        return f'{self.student.email}' 



