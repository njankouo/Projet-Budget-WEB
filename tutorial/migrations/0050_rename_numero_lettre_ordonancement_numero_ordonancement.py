# Generated by Django 5.1 on 2024-10-02 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0049_detailordonancement_ordonancement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordonancement',
            old_name='numero_lettre',
            new_name='numero_ordonancement',
        ),
    ]
