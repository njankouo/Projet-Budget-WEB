# Generated by Django 5.1 on 2024-09-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0013_operation_idparagraphe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='idparagraphe',
            field=models.ManyToManyField(related_name='operations', to='tutorial.paragraphe'),
        ),
    ]
