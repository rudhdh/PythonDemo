# Generated by Django 4.0.6 on 2022-07-31 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Todo',
        ),
    ]
