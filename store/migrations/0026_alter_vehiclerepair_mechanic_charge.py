# Generated by Django 4.2.3 on 2023-10-04 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_remove_vehiclerepairoverview_workshop_need_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclerepair',
            name='mechanic_charge',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
