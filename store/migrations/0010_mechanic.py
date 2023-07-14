# Generated by Django 4.2.3 on 2023-07-14 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0009_vehiclepart_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/images/mechanic')),
                ('vehicle_speciality', models.CharField(choices=[('Bike', 'Bike'), ('Car', 'Car'), ('Semi', 'Semi'), ('Heavy', 'Heavy'), ('Machinery', 'Machinery')], max_length=255)),
                ('vehicle_part_speciality', models.CharField(choices=[('Wheel', 'Wheel'), ('Engine', 'Engine'), ('Body', 'Body'), ('Chassis', 'Chassis'), ('Electricity', 'Electricity'), ('Other', 'Other')], max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]