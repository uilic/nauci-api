from django.contrib import admin

from nauci_service.apps.tutors.models import Tutor


class TutorAdmin(admin.ModelAdmin):
    list_display = ["zemlja_porekla", "oblast_predavanja"]
    search_fields = ["zemlja_porekla", "oblast_predavanja"]
    list_per_page = 20


admin.site.register(Tutor, TutorAdmin)
