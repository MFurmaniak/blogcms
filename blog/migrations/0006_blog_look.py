# Generated by Django 3.1 on 2021-02-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='look',
            field=models.TextField(default='#container img { \nborder-radius: 29px; \nwidth: 100%; \nheight: 360px; \nopacity: 0.7; \nalign-content: center; \n} \n#container img { \nopacity: 1.0; } \na {text-align: center; text-decoration: none;}'),
        ),
    ]
