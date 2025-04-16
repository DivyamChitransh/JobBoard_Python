from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(default='No description provided')
    company_Name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    salary_Range = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} at {self.company_Name}"

