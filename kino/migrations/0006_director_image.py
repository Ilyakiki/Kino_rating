# Generated by Django 4.1.1 on 2022-10-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0005_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='image',
            field=models.FileField(null=True, upload_to='directors'),
        ),
    ]
