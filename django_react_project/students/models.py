from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField("Name",max_length=100)
    email = models.EmailField(max_length=100)
    document = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=100)
    registration_date = models.DateField("Registration Date" ,auto_now_add=True)
    # active = models.BooleanField(default=True)

    def __str__(self):
        return self.name