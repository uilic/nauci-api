from uuid import uuid4

from django.db import models

from nauci_service.apps.core.models import CoreModel


class Tutor(CoreModel):
    zemlja_porekla = models.CharField(max_length=32)
    oblast_predavanja = models.CharField(max_length=32)
    picture = models.FileField(
        "Document", upload_to="media/", blank=True, null=True, max_length=255
    )
