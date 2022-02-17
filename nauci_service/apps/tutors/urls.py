from django.urls import path
from .views import TutorUploadAPIView, CertificateUploadAPIView, EducationUploadAPIView

urlpatterns = [
    path("tutor", TutorUploadAPIView.as_view()),
    path("tutor/certificate", CertificateUploadAPIView.as_view()),
    path("tutor/education", EducationUploadAPIView.as_view()),
]
