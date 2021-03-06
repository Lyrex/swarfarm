# Generated by Django 2.1.7 on 2019-02-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0002_auto_20190220_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='total_slots',
            field=models.IntegerField(default=5, help_text='Maximum monsters combined front/backline.'),
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='id',
            field=models.IntegerField(help_text='ID matches com2us data', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='level',
            name='frontline_slots',
            field=models.IntegerField(default=5),
        ),
        migrations.RemoveField(
            model_name='level',
            name='max_slots',
        ),
        migrations.AlterUniqueTogether(
            name='level',
            unique_together={('dungeon', 'floor', 'difficulty')},
        ),
    ]
