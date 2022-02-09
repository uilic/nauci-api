from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

admin_urlpatterns = [path("admin/", admin.site.urls)]

api_urlpatterns = [
    path(
        "api/auth/",
        include(("nauci_service.apps.accounts.urls", "auth"), namespace="api-auth"),
    ),
    path("_healthcheck/", lambda r: HttpResponse()),
]

urlpatterns = admin_urlpatterns + api_urlpatterns
