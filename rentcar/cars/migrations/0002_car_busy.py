# Generated by Django 3.2.6 on 2022-01-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='busy',
            field=models.BooleanField(default=1, verbose_name='Занята'),
            preserve_default=False,
        ),
    ]