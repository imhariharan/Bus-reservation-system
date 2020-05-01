from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_seats'),
    ]

    operations = [
        migrations.DeleteModel(
            name='otp',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='scanupload',
        ),
        migrations.RemoveField(
            model_name='allbookings',
            name='Phonenumber',
        ),
        migrations.RemoveField(
            model_name='allbookings',
            name='car_number',
        ),
        migrations.AlterField(
            model_name='allbookings',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
