# Generated by Django 5.1 on 2024-10-06 23:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0070_remove_detailordonancement_idprocedure_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boncommande',
            name='idsignataire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.signataire'),
        ),
    ]
