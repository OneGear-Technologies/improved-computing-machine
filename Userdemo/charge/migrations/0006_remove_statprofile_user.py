# Generated by Django 4.1.4 on 2023-01-22 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0005_alter_statprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statprofile',
            name='user',
        ),
    ]
