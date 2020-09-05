# Generated by Django 3.1 on 2020-09-02 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlantChoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genus", models.CharField(max_length=100)),
                ("genus_common_name", models.CharField(max_length=100)),
                ("species", models.CharField(max_length=100)),
                ("species_common_name", models.CharField(max_length=100)),
                (
                    "square_footage",
                    models.DecimalField(
                        decimal_places=2, default=0.25, max_digits=3),
                ),
                (
                    "square_footage_sfg",
                    models.DecimalField(
                        decimal_places=2, default=0.25, max_digits=3),
                ),
                ("additional_information", models.CharField(max_length=100)),
            ],
            options={
                "unique_together": {("species", "additional_information")},
            },
        ),
    ]
