# Generated by Django 4.1.1 on 2022-10-27 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0012_remove_usermodel_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='password',
            new_name='set_password',
        ),
    ]