# Generated by Django 5.2.3 on 2025-06-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='location',
            field=models.CharField(choices=[('cairo', 'Cairo Governorate'), ('giza', 'Giza Governorate'), ('alexandria', 'Alexandria Governorate'), ('fayoum', 'Fayoum Governorate'), ('aswan', 'Aswan Governorate')], max_length=100),
        ),
    ]
