# Generated by Django 5.0.4 on 2024-06-21 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_reservation_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.TimeField(),
        ),
    ]