# Generated by Django 4.1.3 on 2023-01-05 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_mynotes_created_alter_usersignup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 5, 14, 4, 3, 421176)),
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='username',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 5, 14, 4, 3, 420177)),
        ),
    ]
