# Generated by Django 3.2.8 on 2021-10-20 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_auto_20211019_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='course',
            name='is_core',
            field=models.BooleanField(default=True),
        ),
    ]
