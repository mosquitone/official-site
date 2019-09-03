# Generated by Django 2.2.4 on 2019-09-02 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('music', '0002_auto_20190902_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicindexpage',
            name='background_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]