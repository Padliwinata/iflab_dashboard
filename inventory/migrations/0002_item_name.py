# Generated by Django 4.1 on 2023-07-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
