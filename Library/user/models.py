from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
def mai_len_check(val):
    if len(val):
        raise ValidationError("length is less then 10")

    

class Post(models.Model):
    title=models.CharField(validators=[mai_len_check],max_length=29)
    text=models.TextField()
    objects=models.Manager

class PostForm(models.ModelForm):
    class Meta:
        model=Post
        fields=['title']
    

# Create your models here.
