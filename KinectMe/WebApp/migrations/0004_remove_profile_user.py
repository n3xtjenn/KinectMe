# Generated by Django 3.1.2 on 2020-10-08 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_auto_20201008_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
