from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel


@register_snippet
class Member(models.Model):
    japanese_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    part = models.CharField(max_length=255)
    copy = models.CharField(max_length=255)
    japanese_description = models.CharField(max_length=255)
    english_description = models.CharField(max_length=255)
    avator = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    priority = models.IntegerField(default=100)

    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('japanese_name'),
            FieldPanel('english_name'),
        ], heading="name"),
        FieldPanel('copy'),
        FieldPanel('part'),
        MultiFieldPanel([
            FieldPanel('japanese_description'),
            FieldPanel('english_description'),
        ], heading="description"),
        ImageChooserPanel('icon'),
        ImageChooserPanel('avator'),
        FieldPanel('priority'),
        MultiFieldPanel([
            FieldPanel('twitter'),
            FieldPanel('facebook'),
            FieldPanel('instagram'),
        ], heading="SNS"),
    ]

    def __str__(self):
        return self.english_name

    class Meta:
        verbose_name_plural = 'mosquitone member'


@register_snippet
class History(models.Model):
    summary = models.CharField(max_length=32)
    date = models.DateField()
    text = models.CharField(max_length=255)
    by = models.ForeignKey(Member, null=True, blank=True,
                           on_delete=models.CASCADE)

    panels = [
        FieldPanel('summary'),
        FieldPanel('date'),
        FieldPanel('text'),
        FieldPanel('by'),
    ]

    def __str__(self):
        return "{}({})".format(self.summary, self.date)

    class Meta:
        verbose_name_plural = 'mosquitone history'


class AboutPage(Page):
    intro = RichTextField()
    english_history = RichTextField(blank=True)
    japanese_history = RichTextField(blank=True)
    main_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    background_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=False,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('english_history'),
        FieldPanel('japanese_history'),
        ImageChooserPanel('main_image'),
        ImageChooserPanel('background_image'),
    ]

    def get_context(self, request):
        members = Member.objects.order_by('priority')
        histories = History.objects.order_by('date')

        # Update template context
        context = super().get_context(request)
        context['members'] = members
        context['histories'] = histories
        return context
