import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_allbookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_name', models.CharField(blank=True, max_length=50, null=True)),
                ('visiname', models.CharField(blank=True, default='NONE', max_length=50, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(blank=True, choices=[('allow', 'Allow'), ('occupied', 'Occupied')], default='allow', max_length=50)),
            ],
        ),
    ]
