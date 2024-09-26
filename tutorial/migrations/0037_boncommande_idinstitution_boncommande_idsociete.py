# Generated by Django 5.1 on 2024-09-26 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0036_elementcout_conditionnement'),
    ]

    operations = [
        migrations.AddField(
            model_name='boncommande',
            name='idinstitution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.institution'),
        ),
        migrations.AddField(
            model_name='boncommande',
            name='idsociete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.societe'),
        ),
    ]
