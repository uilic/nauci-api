from uuid import uuid4

from django.db import models

from nauci_service.apps.core.models import CoreModel


class Tutor(CoreModel):
    country_of_origin = models.CharField(null=True, max_length=32)
    subject_taught = models.CharField(null=True, max_length=32)
    hourly_rate = models.IntegerField(null=True)
    picture = models.FileField(
        "picture", upload_to="media/", blank=True, null=True, max_length=255
    )
    languages_spoken = models.JSONField(null=True)
    teaching_experience = models.CharField(null=True, max_length=32)
    current_situation = models.CharField(null=True, max_length=32)
    headline = models.CharField(null=True, max_length=32)
    introduce = models.CharField(null=True, max_length=32)
    methodology = models.CharField(null=True, max_length=32)


class Certificate(CoreModel):
    tutor = models.ForeignKey(
        "tutors.Tutor", on_delete=models.CASCADE, related_name="certificates"
    )
    subject = models.CharField(null=True, max_length=32)
    certificate = models.CharField(null=True, max_length=32)
    description = models.CharField(null=True, max_length=300)
    issued_by = models.CharField(null=True, max_length=32)
    years_of_study = models.CharField(null=True, max_length=9)
    document = models.FileField(
        "document", upload_to="media/", blank=True, null=True, max_length=255
    )


class Education(CoreModel):
    tutor = models.ForeignKey(
        "tutors.Tutor", on_delete=models.CASCADE, related_name="education"
    )
    university = models.CharField(null=True, max_length=32)
    degree = models.CharField(null=True, max_length=32)
    degree_type = models.CharField(null=True, max_length=300)
    specialization = models.CharField(null=True, max_length=32)
    years_of_study = models.CharField(null=True, max_length=9)
    diploma = models.FileField(
        "diploma", upload_to="media/", blank=True, null=True, max_length=255
    )
