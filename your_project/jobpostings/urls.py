from django.urls import path
from .views import JobModelCreateView, JobModelListView, JobModelDetailView, JobModelUpdateView, JobModelDeleteView

urlpatterns = [
    path('jobs/', JobModelListView.as_view(), name='jobs-list'),
    path('jobs/create/', JobModelCreateView.as_view(), name='create-job'),
    path('jobs/<int:pk>/', JobModelDetailView.as_view(), name='jobs-details'),
    path('jobs/<int:pk>/update/', JobModelUpdateView.as_view(), name='jobs-update'),
    path('jobs/<int:pk>/delete/', JobModelDeleteView.as_view(), name='jobs-delete'),
]
