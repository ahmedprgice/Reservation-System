# Generated by Django 5.0.6 on 2024-06-21 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_facility_id_alter_facility_facility_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='reviews',
        ),
    ]
