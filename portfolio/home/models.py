from django.db import models

# Create your models here.

class Getdate(models.Model):
    name  = models.CharField(max_length=250)
    user_email = models.EmailField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name