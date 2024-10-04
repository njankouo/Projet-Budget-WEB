# Generated by Django 5.1 on 2024-10-03 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0056_alter_operationdetail_montant_engage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailordonancement',
            old_name='idlettrecommande',
            new_name='idordonancement',
        ),
        migrations.RemoveField(
            model_name='lignelettrecommande',
            name='idboncommande',
        ),
        migrations.AddField(
            model_name='lignelettrecommande',
            name='idlettrecommande',
            field=models.ForeignKey(blank=True, db_column='idboncommande', null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.lettrecommande'),
        ),
    ]
