from rest_framework import serializers
from .models import JobSeeker

class JobSeekerSerialize(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ['id','name','email','skills','resume']