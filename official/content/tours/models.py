from datetime import datetime, timedelta, time
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel


@register_snippet
class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('url'),
    ]

    def __str__(self):
        return self.name


@register_snippet
class Show(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=125, blank=True)
    date = models.DateField()
    location = models.ForeignKey(Location, null=True, blank=True,
                                 on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True)
    information = models.URLField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('date'),
        SnippetChooserPanel('location'),
        FieldPanel('description'),
        FieldPanel('information'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Show'


class ShowIndexPage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=False,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('background_image'),
    ]

    def get_context(self, request):
        today_start = datetime.combine(datetime.today(), time())
        upcomming_show = Show.objects.order_by(
            'date').filter(date__gte=today_start)
        past_show = Show.objects.order_by('-date').filter(date__lt=today_start)

        context = super().get_context(request)
        context['upcomming_show'] = upcomming_show
        context['past_show'] = past_show

        return context
