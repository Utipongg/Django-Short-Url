# Generated by Django 5.0.7 on 2024-08-05 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urldb',
            name='shorturl',
        ),
    ]
