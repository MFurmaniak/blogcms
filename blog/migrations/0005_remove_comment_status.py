# Generated by Django 3.1 on 2021-02-02 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210126_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
    ]
