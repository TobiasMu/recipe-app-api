# Generated by Django 3.2.25 on 2024-06-21 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_minues',
            new_name='time_mintues',
        ),
    ]
