from pydoc import describe
from tabnanny import verbose
from django.db import models
from abstract.models import AbstractDateTime


class Task(AbstractDateTime):
    MAX_LENGHT_TEXT = 255

    describe = models.CharField(
        verbose_name="описание",
        null=False,
        max_length=MAX_LENGHT_TEXT
    )

    todo = models.CharField(
        verbose_name="задание",
        null=False,
        max_length=MAX_LENGHT_TEXT
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="активность",
        null=False,
    )

    def __str__(self) -> str:
        return f"Задание {self.id}: {self.todo}"

    class Meta:
        ordering = (
            'id',
        )
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
