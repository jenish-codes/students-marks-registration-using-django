from django.db import models

class StudentDetails(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    tamil = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    social = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    pass_fail = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)