# Generated by Django 2.2.4 on 2019-08-14 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='showindexpage',
            name='background_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]