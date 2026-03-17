from django.db import models

# Create your models here.


class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.IntegerField()

    def __str__(self):
        return f"{self.fname} - {self.lname}"
