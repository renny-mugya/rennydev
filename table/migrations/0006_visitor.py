# Generated by Django 3.2.8 on 2021-10-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0005_auto_20211021_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('session_key', models.CharField(max_length=255)),
                ('ip_addr', models.CharField(max_length=255)),
            ],
        ),
    ]
