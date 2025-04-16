from rest_framework import serializers
from .models import Employer

class EmployerSerialize(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['company_name','email','mobile','address','skills']