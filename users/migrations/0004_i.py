# Generated by Django 5.0.6 on 2024-06-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_merge_0002_patient_xray_scan_0002_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='i',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
            ],
        ),
    ]
