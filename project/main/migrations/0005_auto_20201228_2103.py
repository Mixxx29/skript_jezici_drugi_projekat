# Generated by Django 3.1.4 on 2020-12-28 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201228_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.project')),
            ],
        ),
    ]
