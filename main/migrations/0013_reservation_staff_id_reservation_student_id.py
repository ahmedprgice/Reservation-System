# Generated by Django 5.0.4 on 2024-06-20 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_reservation_is_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='staff_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.staff'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='student_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student'),
        ),
    ]