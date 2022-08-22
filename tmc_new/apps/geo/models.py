from django.db.models import CharField
from model_utils.models import TimeStampedModel


class Region(TimeStampedModel):
    name = CharField('название', max_length=500, unique=True)

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'
        ordering = ['name']

    def __str__(self):
        return self.name
