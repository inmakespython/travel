from django.db import models

# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pictures')
    description = models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    t_name = models.CharField(max_length=250)
    t_image = models.ImageField(upload_to='pictures')
    t_description = models.TextField()

    def __str__(self):
        return self.t_name













