# Generated by Django 3.2.23 on 2024-02-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_heatlevel_heat_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='staff_favourite',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]