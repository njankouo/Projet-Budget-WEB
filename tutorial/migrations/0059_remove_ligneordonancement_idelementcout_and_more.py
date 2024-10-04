# Generated by Django 5.1 on 2024-10-03 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0058_ligneordonancement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ligneordonancement',
            name='idelementcout',
        ),
        migrations.AlterField(
            model_name='detailordonancement',
            name='idordonancement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.ordonancement'),
        ),
    ]
