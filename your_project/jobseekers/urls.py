from django.urls import path
from .views import JobSeekerCreateView, JobSeekerListView, JobSeekerDetailView, JobSeekerUpdateView, JobSeekerDeleteView

urlpatterns = [
    path('jobseekers/', JobSeekerListView.as_view(), name='jobseeker-list'),
    path('jobseekers/create/', JobSeekerCreateView.as_view(), name='jobseeker-create'),
    path('jobseekers/<int:pk>/', JobSeekerDetailView.as_view(), name='jobseeker-detail'),
    path('jobseekers/<int:pk>/update/', JobSeekerUpdateView.as_view(), name='jobseeker-update'),
    path('jobseekers/<int:pk>/delete/', JobSeekerDeleteView.as_view(), name='jobseeker-delete'),
]
