# Generated by Django 3.2.18 on 2023-04-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_remove_booking_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(),
        ),
    ]
