# Generated by Django 2.2.4 on 2019-09-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_musicindexpage_background_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musicpage',
            old_name='bandcamp_url',
            new_name='bandcamp_album_url',
        ),
        migrations.RemoveField(
            model_name='musicindexpage',
            name='background_image',
        ),
        migrations.AddField(
            model_name='musicpage',
            name='bandcamp_player_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
