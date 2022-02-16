from rest_framework import serializers

from nauci_service.apps.tutors.models import Tutor


class ClientTutorUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ["picture", "zemlja_porekla", "oblast_predavanja"]
