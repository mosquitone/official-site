from .base import *

import dj_database_url
import os

DEBUG = False

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

# aws settings
AWS_STORAGE_BUCKET_NAME = 'mosquitone-official-site'
AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = env['AWS_CLOUDFRONT_ALIAS']
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'must-revalidate,public,max-age=31536000',
}
AWS_DEFAULT_ACL = 'public-read'
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
OFFICIAL_JQUERY_USE_CDN = True

COMPRESS_ENABLED = True

GA_TRACKING_ID = env['GA_TRACKING_ID']
