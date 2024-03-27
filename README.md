## document-manager
A simple document manager to store media files in S3 storage bucket.

### Features :
Package contains just a single model to store file that will be stored in S3 bucket with below configurations done.

### Installation guide :
```
pip install git+https://github.com/Assystant/document-manager.git
```

### Configure settings.py :
```
import os

INSTALLED_APPS = [
  .
  .
  'doc_manager',
  'rest_framework',
]


if os.getenv('STORAGE', '') == 'S3':
    INSTALLED_APPS += ['storages',]
    
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', '')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    STORAGES = {
        "default": {
            "BACKEND": 'doc_manager.storage_backends.MediaStorage',
            "OPTIONS": {
            },
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    
    # DEFAULT_FILE_STORAGE = 'doc_manager.storage_backends.MediaStorage'
    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
```

### Update urls.py :
```
urlpatterns = [
  .
  .
  path('', include('doc_manager.urls')),
]
```
