# Generated by Django 2.0.13 on 2019-07-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190702_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Name'),
        ),
    ]
