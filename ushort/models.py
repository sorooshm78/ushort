import hashlib

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
class UrlShort(models.Model):
    url = models.URLField(unique=True)
    hash = models.CharField(max_length=8, unique=True)
    visitor = models.IntegerField(default=0)

    def __str__(self):
        return self.hash

    def add_visitor(self):
        self.visitor += 1
        self.save()


@receiver(pre_save, sender=UrlShort)
def create_hash(sender, instance, **kwargs):
    url = instance.url
    hash = hashlib.md5(url.encode()).hexdigest()[:8]
    instance.hash = hash
