from rest_framework import generics
from .models import JobPost
from .serializers import JobModelSerialize

class JobModelCreateView(generics.CreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobModelSerialize

class JobModelListView(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobModelSerialize

class JobModelDetailView(generics.RetrieveAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobModelSerialize

class JobModelUpdateView(generics.UpdateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobModelSerialize

class JobModelDeleteView(generics.DestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobModelSerialize
