from django.urls import path
from .views import EmployerCreateView, EmployerListView, EmployerDetailView, EmployerUpdateView, EmployerDeleteView

urlpatterns = [
    path('Employers/', EmployerListView.as_view(), name='employers-list'),
    path('Employers/create/', EmployerCreateView.as_view(), name='employers-create'),
    path('Employers/<int:pk>/', EmployerDetailView.as_view(), name='employers-detail'),
    path('Employers/<int:pk>/update/', EmployerUpdateView.as_view(), name='employers-update'),
    path('Employers/<int:pk>/delete/', EmployerDeleteView.as_view(), name='employers-delete'),
]
