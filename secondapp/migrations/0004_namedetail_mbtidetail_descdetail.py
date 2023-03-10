# Generated by Django 4.1 on 2023-01-06 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("file", "0001_initial"),
        ("secondapp", "0003_delete_detail"),
    ]

    operations = [
        migrations.CreateModel(
            name="NameDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="file.mbtidata"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MbtiDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mbti",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="file.mbtidata"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DescDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "desc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="file.mbtidata"
                    ),
                ),
            ],
        ),
    ]
