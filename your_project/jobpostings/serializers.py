from rest_framework import serializers
from .models import JobPost

class JobModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['title','description','company_Name','location','salary_Range']