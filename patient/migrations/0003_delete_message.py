# Generated by Django 4.2.6 on 2023-11-26 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]