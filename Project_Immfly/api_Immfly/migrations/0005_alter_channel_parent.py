# Generated by Django 4.2 on 2023-05-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_Immfly', '0004_remove_channel_parent_channel_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='parent',
            field=models.ManyToManyField(blank=True, related_name='children', to='api_Immfly.channel'),
        ),
    ]
