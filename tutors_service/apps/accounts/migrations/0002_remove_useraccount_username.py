# Generated by Django 4.0.1 on 2022-02-03 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [migrations.RemoveField(model_name="useraccount", name="username")]
