# Generated by Django 2.0.13 on 2019-06-30 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190627_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Name (optional) :')),
                ('email', models.CharField(max_length=256, verbose_name='Email: ')),
            ],
        ),
    ]
