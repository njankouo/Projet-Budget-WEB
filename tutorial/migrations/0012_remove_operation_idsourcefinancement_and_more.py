# Generated by Django 5.1 on 2024-09-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0011_remove_typefinancement_idnaturetache_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='idsourcefinancement',
        ),
        migrations.AddField(
            model_name='operation',
            name='idsourcefinancement',
            field=models.ManyToManyField(null=True, to='tutorial.sourcefinacement'),
        ),
    ]
