from django.db import models


# Create your models here.
class Consent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    english_title = models.CharField(max_length=200)
    english_content = models.TextField(blank=True)
    french_title = models.CharField(max_length=200)
    french_content = models.TextField(blank=True)
    is_every_appraisal = models.BooleanField(default=False)
    allow_more_consent = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
