# Generated by Django 4.2.3 on 2023-07-12 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_vehicle_type_vehiclecategory_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclecategory',
            name='type',
        ),
    ]
