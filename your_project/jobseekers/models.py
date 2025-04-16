from django.db import models

class JobSeeker(models.Model):
    name = models.CharField(max_length=100,default="Unnamed")
    email = models.EmailField(unique=True)
    skills = models.JSONField(default=list)
    resume = models.URLField()

    def __str__(self):
        return self.name

