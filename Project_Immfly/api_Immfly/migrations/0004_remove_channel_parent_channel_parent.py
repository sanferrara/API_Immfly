# Generated by Django 4.2 on 2023-05-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_Immfly', '0003_alter_channel_langueage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='parent',
        ),
        migrations.AddField(
            model_name='channel',
            name='parent',
            field=models.ManyToManyField(blank=True, null=True, related_name='children', to='api_Immfly.channel'),
        ),
    ]
