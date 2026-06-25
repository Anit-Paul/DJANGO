from django.db import models
from django.utils import timezone
# Create your models here.
class Student(models.Model):
    MY_SCHOOL=[
        ('AB','AB School'),
        ('BB','BB School'),
        ('CB','CB School'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos/')
    date=models.DateTimeField(default=timezone.now)
    school=models.CharField(max_length=2,choices=MY_SCHOOL)