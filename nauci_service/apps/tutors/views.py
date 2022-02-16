import logging

from rest_framework.generics import ListCreateAPIView
from botocore.exceptions import ClientError as BotoCoreS3ClientError
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from nauci_service.apps.tutors.models import Tutor
from nauci_service.apps.tutors.serializers import ClientTutorUploadSerializer

LOG = logging.getLogger(__name__)


class ClientDocumentUploadAPIView(ListCreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = ClientTutorUploadSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            tutor = serializer.save()
        except BotoCoreS3ClientError as exc:
            LOG.exception(str(exc), exc_info=exc)
            return Response(status=status.HTTP_424_FAILED_DEPENDENCY)

        response_context = ClientTutorUploadSerializer(tutor).data

        return Response(data=response_context, status=status.HTTP_201_CREATED)
