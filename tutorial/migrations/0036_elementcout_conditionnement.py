# Generated by Django 5.1 on 2024-09-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0035_alter_boncommande_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementcout',
            name='conditionnement',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
