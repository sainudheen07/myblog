# Generated by Django 3.2.3 on 2021-07-28 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='date',
            field=models.DateTimeField(default=datetime.date(2021, 7, 29)),
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
