from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=254)
    roll=models.CharField(max_length=10,unique=True)
    blood_group=models.CharField(max_length=5,blank=True,null=True)
    def __str__(self):
        return self.roll
    class Meta:
        ordering=['roll']

class MobileNumber(models.Model):

    mobile=models.CharField(max_length=10,unique=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.student.name
    class Meta:
        ordering=['mobile']



# Create your models here.
