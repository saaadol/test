# Generated by Django 3.2.6 on 2022-05-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gateway_serialnumber', models.CharField(max_length=20)),
                ('DeviceName', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=20)),
                ('baud_rate', models.CharField(max_length=20)),
                ('connection_type', models.CharField(choices=[('Rs485', 'Rs485'), ('lora', 'lora'), ('Other', 'Other')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gatewayname', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=20)),
                ('list_devices', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('ONGRID', 'ONGRID'), ('PV', 'PV'), ('HYBRID', 'HYBRID')], max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('list_gateway', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('etude', 'Etude'), ('online', 'Online'), ('Other', 'Other')], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='role',
        ),
    ]
