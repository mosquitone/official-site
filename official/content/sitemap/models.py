from django.db import models

from wagtail.core.models import Page
from official.content.home.models import HomePage


class SitemapPage(Page):
    @staticmethod
    def get_tree(page):
        return [(page, [SitemapPage.get_tree(child_page) for child_page in page.get_children().filter(show_in_menus=True)])]

    def get_context(self, request, *args, **kwargs):
        home_page = HomePage.objects.last()
        page_tree = SitemapPage.get_tree(home_page)
        context = super().get_context(request, *args, **kwargs)
        context.update({'page_tree': page_tree})
        return context
