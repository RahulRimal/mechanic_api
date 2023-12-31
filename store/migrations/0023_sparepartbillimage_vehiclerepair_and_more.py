# Generated by Django 4.2.3 on 2023-10-03 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_mechanic_status_vehiclerepairprocess'),
    ]

    operations = [
        migrations.CreateModel(
            name='SparePartBillImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='store/images/vehicle_repair')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleRepair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mechanic_charge', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='store.customer')),
                ('mechanic', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='store.mechanic')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='store.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleRepairOverview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=255)),
                ('problem_description', models.TextField()),
                ('mechanic_charge', models.CharField(max_length=255)),
                ('workshop_need', models.CharField(max_length=255)),
                ('needs_to_tow', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('woner_name', models.CharField(max_length=255)),
                ('woner_name_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='VehicleRepairProcess',
        ),
        migrations.AddField(
            model_name='vehiclerepair',
            name='workshop',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.workshop'),
        ),
        migrations.AddField(
            model_name='sparepartbillimage',
            name='vehicle_repair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.vehiclerepair'),
        ),
    ]
