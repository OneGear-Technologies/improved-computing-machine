# Generated by Django 4.1.4 on 2023-01-14 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_wallet_mo_alter_wallet_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='mo',
        ),
    ]
