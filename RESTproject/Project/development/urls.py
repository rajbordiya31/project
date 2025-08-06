from django.urls import path
from .views import StudentListCreate, StudentDetail
urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
]