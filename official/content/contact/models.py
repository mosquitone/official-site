from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel


@register_snippet
class SorcialNetworkAccount(models.Model):
    sns_name = models.CharField(max_length=50)
    sns_icon_name = models.CharField(max_length=50)
    account_name = models.CharField(max_length=50)
    account_url = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=50)
    priority = models.IntegerField(default=100)

    panels = [
        MultiFieldPanel([
            FieldPanel('sns_name'),
            FieldPanel('sns_icon_name'),
        ], heading="SNS"),
        MultiFieldPanel([
            FieldPanel('account_name'),
            FieldPanel('account_url'),
        ], heading="Account"),
        FieldPanel('description'),
        FieldPanel('priority'),
    ]

    def __str__(self):
        return self.sns_name

    class Meta:
        verbose_name_plural = 'Social Network Service Account'


class ContactPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
    ]
