from django.contrib import admin

from tutors_service.apps.accounts.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name"]
    search_fields = ["email", "first_name"]
    list_per_page = 20


admin.site.register(UserAccount, UserAccountAdmin)
