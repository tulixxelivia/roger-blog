# Generated by Django 2.0.13 on 2019-06-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190626_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=0, upload_to='img'),
            preserve_default=False,
        ),
    ]
