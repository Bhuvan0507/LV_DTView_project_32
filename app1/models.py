from django.db import models

# Create your models here.

from django.urls import reverse

class School(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sprincipale=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)

    def __str__(self):
        return self.sname
    
    def get_absolute_url(self):
        return reverse('School_details',kwargs={'sname':self.sname})
    
class Student(models.Model):
    stname=models.CharField(max_length=100)
    sage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='all_students')

    def __str__(self):
        return self.stname