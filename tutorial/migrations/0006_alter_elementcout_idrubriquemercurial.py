# Generated by Django 5.1 on 2024-09-07 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0005_remove_elementcout_idimputation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementcout',
            name='idrubriquemercurial',
            field=models.ForeignKey(blank=True, db_column='idrubriquemercuriale', null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.rubrique'),
        ),
    ]
