# Generated by Django 4.2.7 on 2023-12-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.png", upload_to="profile_pics"),
        ),
    ]
