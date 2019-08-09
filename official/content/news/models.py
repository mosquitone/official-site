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


class NewsIndexPage(RoutablePageMixin, Page):
    intro = RichTextField(blank=True)
    background_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=False,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('background_image'),
    ]

    def get_context(self, request):
        # Update template context
        context = super().get_context(request)
        context['tag'] = self.tag
        context['newspages'] = self.news
        return context

    def get_news(self):
        return NewsPage.objects.order_by('-date')

    @route(r'^tag/(?P<tag>.+)/$')
    def news_by_tag(self, request, tag, *args, **kwargs):
        self.tag = tag
        self.news = self.get_news().filter(tags__name=tag)
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^$')
    def news_list(self, request, *args, **kwargs):
        self.tag = None
        self.news = self.get_news()
        return Page.serve(self, request, *args, **kwargs)


class NewsPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'NewsPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class NewsPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=NewsPageTag, blank=True)
    categories = ParentalManyToManyField('news.NewsCategory', blank=True)
    author = models.ForeignKey(
        Member, null=True, blank=True, on_delete=models.SET_NULL)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    @property
    def news_index_page(self):
        return self.get_parent().specific

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="News information"),
        # FieldPanel('author'),
        SnippetChooserPanel('author'),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class NewsPageGalleryImage(Orderable):
    page = ParentalKey(NewsPage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


@register_snippet
class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'news categories'
