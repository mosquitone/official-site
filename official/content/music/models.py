from django.db import models

# Create your models here.

from django import forms
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel)
from wagtail.core.fields import RichTextField
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from official.content.about.models import Member


class MusicIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['music_pages'] = MusicPage.objects.order_by('-release_date')
        return context


class MusicPage(Page):
    release_date = models.DateField("Release date")
    copy = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    artwork = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=False,
        on_delete=models.SET_NULL, related_name='artwork'
    )
    bandcamp_album_url = models.URLField(null=True, blank=True)
    bandcamp_player_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)

    @property
    def music_index_page(self):
        return self.get_parent().specific

    search_fields = Page.search_fields + [
        index.SearchField('copy'),
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('release_date'),
            ImageChooserPanel('artwork'),
        ], heading="Music information"),
        FieldPanel('copy'),
        FieldPanel('description'),
        FieldPanel('youtube_url'),
        FieldPanel('bandcamp_album_url'),
        FieldPanel('bandcamp_player_url'),
        InlinePanel('tracks', label="Tracks"),
    ]


class MusicTrack(Orderable):
    page = ParentalKey(MusicPage, on_delete=models.CASCADE,
                       related_name='tracks')
    title = models.CharField(blank=False, max_length=250)
    duration = models.DurationField()

    panels = [
        FieldPanel('title'),
        FieldPanel('duration'),
    ]
