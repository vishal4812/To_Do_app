# Generated by Django 3.0.4 on 2020-04-24 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='compile',
            new_name='complete',
        ),
    ]
