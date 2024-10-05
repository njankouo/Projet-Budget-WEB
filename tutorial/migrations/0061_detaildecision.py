# Generated by Django 5.1 on 2024-10-05 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0060_rename_code_signataire_adresse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailDecision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idactivite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.activite')),
                ('iddecision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.decision')),
                ('idoperation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.operation')),
                ('idparagraphe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.paragraphe')),
                ('idprocedure', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.procedure')),
                ('idsousprogramme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.sousprogramme')),
                ('idstructure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.structure')),
                ('idtache', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.tache')),
            ],
        ),
    ]
