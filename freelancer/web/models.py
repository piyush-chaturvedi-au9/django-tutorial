from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    picture = models.ImageField(upload_to='contacts', null=True)

    def __str__(self):
        return self.email