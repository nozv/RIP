# Generated by Django 4.0 on 2022-01-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vet', '0002_service_description_service_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
            ],
        ),
    ]