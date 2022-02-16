from django.urls import path
from .views import ClientDocumentUploadAPIView

urlpatterns = [path("tutor", ClientDocumentUploadAPIView.as_view())]
