from django.contrib.gis.db import models as geo_models
from django.contrib.gis.geos import Point
from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User


class Media(models.Model):
    media_file = models.ImageField(_('file'), upload_to='media/profiles/media/')
    location = geo_models.PointField(_('location'), blank=True, default=Point(0, 0))  # or Point([])
    location_str = models.CharField(_('location str'), max_length=150, blank=True)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('Media File')
        verbose_name_plural = _('Media Files')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.OneToOneField(Media, blank=True, null=True, on_delete=models.CASCADE)
    content = models.CharField(_('content'), max_length=280, blank=True)
    location = geo_models.PointField(
        _('location'),
        blank=True,
        # patial_index=False,
        default=Point(0, 0),  # or Point([])
    )
    location_str = models.CharField(_('location str'), max_length=150, blank=True)
    favorites_count = models.IntegerField(_('favorites count'), default=0)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('Reaction')
        verbose_name_plural = _('Reactions')
