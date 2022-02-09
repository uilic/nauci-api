from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from nauci_service.apps.core.models import CoreModel


class UserManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        if not kwargs.get("email", None):
            raise ValueError("Users must give an email address")

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserAccount(PermissionsMixin, CoreModel, AbstractBaseUser):

    email = models.EmailField(verbose_name="Email", max_length=128, unique=True)
    first_name = models.CharField(
        verbose_name="First name", max_length=30, blank=True, null=True
    )
    last_name = models.CharField(
        verbose_name="Last name", max_length=30, blank=True, null=True
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
    )
    is_tutor = models.BooleanField(
        "is tutor", default=False, help_text="Designates whether this user is a tutor."
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("first_name", "last_name")

    def __str__(self):
        return self.email

    def get_short_name(self) -> str:
        return str(self.email)

    def get_full_name(self) -> str:
        if self.first_name and self.last_name:
            full_name = f"{self.first_name} {self.last_name} <{self.email}>"
        else:
            full_name = self.get_short_name()
        return full_name
