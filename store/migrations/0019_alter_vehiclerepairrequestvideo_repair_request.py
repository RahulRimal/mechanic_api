# Generated by Django 4.2.3 on 2023-07-14 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_vehiclerepairrequest_vehiclerepairrequestvideo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclerepairrequestvideo',
            name='repair_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='store.vehiclerepairrequest'),
        ),
    ]
