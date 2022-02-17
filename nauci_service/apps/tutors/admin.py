from django.contrib import admin

from nauci_service.apps.tutors.models import Education, Certificate, Tutor


class TutorAdmin(admin.ModelAdmin):
    list_display = [
        "subject_taught",
        "picture",
        "country_of_origin",
        "hourly_rate",
        "languages_spoken",
        "teaching_experience",
        "current_situation",
    ]
    search_fields = ["country_of_origin", "subject_taught"]
    list_per_page = 20


class CertificateAdmin(admin.ModelAdmin):
    list_display = [
        "subject",
        "certificate",
        "description",
        "issued_by",
        "years_of_study",
        "document",
    ]
    search_fields = ["subject"]
    list_per_page = 20


class EducationAdmin(admin.ModelAdmin):
    list_display = [
        "university",
        "degree",
        "degree_type",
        "specialization",
        "years_of_study",
        "diploma",
    ]
    search_fields = ["university"]
    list_per_page = 20


admin.site.register(Tutor, TutorAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Education, EducationAdmin)
