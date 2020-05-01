# Generated by Django 3.0.1 on 2020-03-23 11:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='otp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('otp', models.CharField(blank=True, max_length=5, null=True)),
                ('visiname', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='scanupload',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slot_name', models.CharField(blank=True, max_length=50, null=True)),
                ('visiname', models.CharField(blank=True, default='NONE', max_length=50, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(blank=True, choices=[('allow', 'Allow'), ('occupied', 'Occupied')], default='allow', max_length=50)),
                ('car_number', models.CharField(blank=True, max_length=50, null=True)),
                ('Phonenumber', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.TextField(blank=True, max_length=500)),
                ('Phonenumber', models.CharField(blank=True, max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]