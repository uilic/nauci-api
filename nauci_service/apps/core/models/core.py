from uuid import uuid4

from django.db import models


class CoreModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_on = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="created"
    )
    last_updated_on = models.DateTimeField(auto_now=True, verbose_name="updated")

    class Meta:
        abstract = True
        ordering = ("created_on",)

    def __str__(self):
        return str(self.pk)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.pk}>"
