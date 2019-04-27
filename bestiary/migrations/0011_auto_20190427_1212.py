# Generated by Django 2.1.7 on 2019-04-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0010_auto_20190318_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='dungeon',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dungeon',
            name='icon',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
