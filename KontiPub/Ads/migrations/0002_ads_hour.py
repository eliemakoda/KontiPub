# Generated by Django 3.1.6 on 2024-03-18 00:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='hour',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
