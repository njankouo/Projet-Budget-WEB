# Generated by Django 5.1 on 2024-09-14 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0022_utilisateur_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='annee',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
