# Generated by Django 4.0.2 on 2022-02-16 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tutors", "__first__"),
        ("accounts", "0003_remove_useraccount_telephone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="tutor",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="account",
                to="tutors.tutor",
            ),
        )
    ]
