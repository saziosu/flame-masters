# Generated by Django 3.2.23 on 2024-01-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240127_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='heatlevel',
            name='heat_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
