from django.db import models

from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=254)
    roll=models.CharField(max_length=10,unique=True)
    blood_group=models.CharField(max_length=5,blank=True,null=True)
    def __str__(self):
        return self.roll
    class Meta:
        ordering=['roll']

    def get_mobileNumber(self):
        l=MobileNumber.objects.filter(student_id=self.id)
        return l



class MobileNumber(models.Model):
    mobile=models.CharField(max_length=10,unique=True)


    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="mobiledata")
    def __str__(self):
        return self.student.name
    class Meta:
        ordering=['mobile']



# Create your models here.






class publication(models.Model):
    title=models.CharField(max_length=25)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['title']
    
class  Article(models.Model):

    headline = models.CharField(max_length=100)
    publications=models.ManyToManyField(publication)
    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline





class Exam(models.Model):
    s_name=models.CharField(max_length=36)
    uid=models.CharField(max_length=10,primary_key=True)
    mobile_no=models.IntegerField(max_length=10)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.uid
    
    class Meta:
        ordering = ['uid']





# Create your models here.
