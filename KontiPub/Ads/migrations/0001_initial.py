# Generated by Django 3.1.6 on 2024-03-18 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=400)),
                ('feature', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(default='cameroun', max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=100)),
                ('date_event', models.DateField()),
                ('avatar', models.ImageField(upload_to='images/')),
                ('added_date', models.DateField(auto_now_add=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ads.administrateur')),
            ],
        ),
    ]
