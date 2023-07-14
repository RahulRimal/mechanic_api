# Generated by Django 4.2.3 on 2023-07-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_mechanic_vehicle_part_speciality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclepart',
            name='name',
            field=models.CharField(choices=[('wheel', 'Wheel'), ('engine', 'Engine'), ('body', 'Body'), ('chassis', 'Chassis'), ('electricity', 'Electricity'), ('other', 'Other')], max_length=100),
        ),
    ]
