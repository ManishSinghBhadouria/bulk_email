# Generated by Django 3.0.2 on 2020-04-20 09:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('sem', models.CharField(max_length=100)),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
