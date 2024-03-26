from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Document(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    title = models.CharField(max_length=500, blank=True, default='')
    file = models.FileField(blank=True, upload_to="documents/")
