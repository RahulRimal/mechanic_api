# Generated by Django 4.2.3 on 2023-07-14 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_vehiclepart_alter_customer_image_alter_vehicle_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclepart',
            name='vehicle',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='store.vehicle'),
            preserve_default=False,
        ),
    ]
