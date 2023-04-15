from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirmPassword = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField()
    #gender = models.RadioField()
    birth_date = models.DateField()
    #class_stream = models.SelectField()
    #class_year = models.SelectField()


