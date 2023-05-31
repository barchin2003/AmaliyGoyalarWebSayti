from django.db import models


# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='idea/')
    body = models.TextField()

    def __str__(self):
        return self.title
