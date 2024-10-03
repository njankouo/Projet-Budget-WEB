# Generated by Django 5.1 on 2024-10-02 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0048_operation_idannee'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailOrdonancement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idactivite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.activite')),
                ('idlettrecommande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.lettrecommande')),
                ('idoperation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.operation')),
                ('idparagraphe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.paragraphe')),
                ('idprocedure', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.procedure')),
                ('idsousprogramme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.sousprogramme')),
                ('idstructure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.structure')),
                ('idtache', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.tache')),
            ],
        ),
        migrations.CreateModel(
            name='Ordonancement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_lettre', models.CharField(max_length=255, null=True)),
                ('status', models.IntegerField(default=0)),
                ('idinstitution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.institution')),
                ('idir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.ir')),
                ('idsociete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.societe')),
                ('idtva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.tva')),
            ],
        ),
    ]
