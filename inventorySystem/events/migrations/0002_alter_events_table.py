# Generated by Django 5.2 on 2025-04-10 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='events',
            table='events_events',
        ),
    ]
