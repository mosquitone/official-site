from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    background_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=False,
        on_delete=models.SET_NULL, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('background_image'),
    ]
