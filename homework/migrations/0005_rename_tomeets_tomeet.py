# Generated by Django 3.2.12 on 2022-05-05 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_alter_tomeets_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToMeets',
            new_name='ToMeet',
        ),
    ]
