# Generated by Django 4.2.6 on 2023-12-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_alter_clinicinfo_telephone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicinfo',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
