# Generated by Django 5.1 on 2024-10-06 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0067_lettrecommande_idprocedure'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordonancement',
            name='idprocedure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.procedure'),
        ),
    ]
