# Generated by Django 2.2.4 on 2019-08-16 18:08

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_aboutpage_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]