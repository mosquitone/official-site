from django.db import models
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         PageChooserPanel)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    background_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=False,
        on_delete=models.SET_NULL, related_name='+'
    )
    primary_button_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    primary_button_text = models.CharField(
        null=True, blank=True, max_length=25)
    secondary_button_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    secondary_button_text = models.CharField(
        null=True, blank=True, max_length=25)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('background_image'),
        MultiFieldPanel([
            FieldPanel('primary_button_text'),
            PageChooserPanel('primary_button_link'),
        ], heading="primary button"),
        MultiFieldPanel([
            FieldPanel('secondary_button_text'),
            PageChooserPanel('secondary_button_link'),
        ], heading="secondary button"),
    ]
