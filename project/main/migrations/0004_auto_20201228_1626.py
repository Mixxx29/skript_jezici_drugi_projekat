# Generated by Django 3.1.4 on 2020-12-28 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201227_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
    ]
