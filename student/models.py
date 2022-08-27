from django.db import models

# Create your models here.
class studreg(models.Model):
    sname=models.CharField(max_length=200,null=True)
    admno=models.IntegerField()
    department=models.CharField(max_length=200,null=True)
    year=models.IntegerField()
    course=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    contactno=models.IntegerField()

class parreg(models.Model):
    username=models.CharField(max_length=200,null=True)
    admno=models.IntegerField()
    department=models.CharField(max_length=200,null=True)
    sname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    contactno=models.IntegerField()
    

class addteach(models.Model):
    username=models.CharField(max_length=200,null=True)
    tid=models.IntegerField(null=True)
    department=models.CharField(max_length=200,null=True)
    year=models.IntegerField(null=True)
    course=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    contactno=models.IntegerField(null=True)


class eventadd(models.Model):
    eventname=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True)
    date=models.DateField()
    day=models.IntegerField()
    time=models.TimeField()
    

class leave(models.Model):
    name=models.CharField(max_length=200,null=True)
    admno=models.IntegerField(null=True)
    department=models.CharField(max_length=200,null=True)
    date=models.DateField(null=True)
    days=models.IntegerField(null=True)
    reason=models.CharField(max_length=200,null=True)
    status=models.BooleanField(default=False)
    



        
