from django.db import models

# Create your models here.


class account(models.Model):
        firstName = models.CharField(max_length=100)
        lastName = models.CharField(max_length=100)
        Email = models.CharField(max_length=100)
        Address = models.CharField(max_length=100)
        BirthDate = models.CharField(max_length=100)
        Phone = models.CharField(max_length=100)
        Course = models.CharField(max_length=100)
        Specialization = models.CharField(max_length=100)
        Password = models.CharField(max_length=100)

        def __str__(self):
            return self.firstName + " " + self.lastName
