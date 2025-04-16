from django.db import models

class Employer(models.Model):
    company_name = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(unique=True, blank=False,null=False)
    mobile = models.CharField(max_length=12,blank=True, null=True)
    address = models.CharField(max_length=200,blank=False,null=False)
    skills = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return self.company_name
    

