from django.conf import settings

from official.content.contact.models import SorcialNetworkAccount
from official.content.music.models import MusicPage

def django_settings(request):
    return {
        'settings': settings,
    }

def sns_accounts(request):
    return {
        'sns_accounts': SorcialNetworkAccount.objects.order_by('priority'),
        'music_pages': MusicPage.objects.order_by('-release_date'),
    }
