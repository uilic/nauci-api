# Generated by Django 4.0.2 on 2022-02-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("tutors", "0003_remove_tutor_oblast_predavanja_and_more")]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="certificate",
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="certificate",
            name="description",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="certificate",
            name="issued_by",
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="certificate",
            name="years_of_study",
            field=models.CharField(max_length=9, null=True),
        ),
    ]
