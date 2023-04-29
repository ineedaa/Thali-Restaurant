# Generated by Django 3.2.18 on 2023-04-29 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_bookingdetails_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='BookingDetails',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
