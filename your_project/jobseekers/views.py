from rest_framework import generics
from .models import JobSeeker
from .serializers import JobSeekerSerialize

class JobSeekerCreateView(generics.CreateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerialize

class JobSeekerListView(generics.ListAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerialize

class JobSeekerDetailView(generics.RetrieveAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerialize

class JobSeekerUpdateView(generics.UpdateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerialize

class JobSeekerDeleteView(generics.DestroyAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerialize
