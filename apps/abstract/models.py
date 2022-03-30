from django.db import models
from datetime import datetime, timedelta


class AbstractDateTime(models.Model):
    datetime_created = models.DateTimeField(
        verbose_name='время создания',
        auto_now_add=True
    )
    datetime_deleted = models.DateTimeField(
        verbose_name='время удаления',
        null=True,
        blank=True,
        auto_now=True
    )
    datetime_live = models.DateTimeField(
        verbose_name="время удаления",
        null=True,
        blank=True,
        auto_now=True
    )

    class Meta:
        abstract = True
