from rest_framework import serializers

from nauci_service.apps.tutors.models import Education, Certificate, Tutor


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "uuid",
            "subject",
            "certificate",
            "description",
            "issued_by",
            "years_of_study",
            "document",
            "tutor",
        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "uuid",
            "university",
            "degree",
            "degree_type",
            "specialization",
            "years_of_study",
            "diploma",
            "tutor",
        ]


class ClientTutorUploadSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True)
    education = EducationSerializer(many=True)

    class Meta:
        model = Tutor
        fields = [
            "uuid",
            "picture",
            "country_of_origin",
            "subject_taught",
            "hourly_rate",
            "languages_spoken",
            "teaching_experience",
            "current_situation",
            "certificates",
            "education",
            "headline",
            "introduce",
            "methodology",
        ]
