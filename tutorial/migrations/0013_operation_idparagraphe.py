# Generated by Django 5.1 on 2024-09-12 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0012_remove_operation_idsourcefinancement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='idparagraphe',
            field=models.ManyToManyField(null=True, to='tutorial.paragraphe'),
        ),
    ]
