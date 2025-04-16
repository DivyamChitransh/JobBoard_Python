from rest_framework import generics
from .models import Employer
from .serializers import EmployerSerialize

class EmployerCreateView(generics.CreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerialize

class EmployerListView(generics.ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerialize

class EmployerDetailView(generics.RetrieveAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerialize

class EmployerUpdateView(generics.UpdateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerialize

class EmployerDeleteView(generics.DestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerialize
