# Generated by Django 4.1 on 2023-01-06 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("secondapp", "0002_remove_detail_name_detail_content"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Detail",
        ),
    ]
