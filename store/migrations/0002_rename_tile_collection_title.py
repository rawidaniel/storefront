# Generated by Django 5.0.4 on 2024-04-23 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='tile',
            new_name='title',
        ),
    ]
